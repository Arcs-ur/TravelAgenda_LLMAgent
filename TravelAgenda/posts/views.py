from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,ListAPIView

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 

from django.db.models import Q
from .serializers import PostSerializer, ImageSerializer, PostSendSerializer
from .models import Post, Image
from .forms import PostForm

# 查看所有用户的帖子
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/post_list.html'  
    context_object_name = 'posts'  
    ordering = ['-created_at']  
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return queryset

# 查看自己的帖子
class MyPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/my_post.html'  
    context_object_name = 'posts'  
    ordering = ['-created_at']  
    paginate_by = 10
    def get_queryset(self):
        queryset = Post.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return queryset
    
# 用户新增帖子
class PostSendView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/send.html'
    
    def form_valid(self, form):
        serializer = PostSendSerializer(data={
            'title': form.cleaned_data['title'],
            'content': form.cleaned_data['content'],
            'images': self.request.FILES.getlist('images')
        })
        
        if serializer.is_valid():
            serializer.save(user=self.request.user) 
            return redirect('posts:post_list')
        return self.form_invalid(form, serializer.errors)
    
    def form_invalid(self, form, errors=None):
        context = self.get_context_data(form=form)
        if errors:
            form.errors.update(errors)
        return self.render_to_response(context)
    
    # def get_success_url(self):
    #     return reverse('posts:post_detail', kwargs={'pk': self.object.pk})

# 每个帖子的详情展示页面
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context




@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('posts:post_list'))

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 检查当前用户是否是发布者，防止其他用户删除帖子
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    post.delete()
    return redirect(reverse('posts:my_post'))

@login_required
def batch_delete_posts(request):
    if request.method == 'POST':
        # 获取提交的选中的帖子ID列表
        selected_post_ids = request.POST.get('selected_posts').split(',')

        # 获取这些帖子，并确保只删除当前用户发布的帖子
        posts_to_delete = get_list_or_404(Post, id__in=selected_post_ids, user=request.user)

        # 删除选中的帖子
        for post in posts_to_delete:
            post.delete()

        # 删除后重定向到帖子列表页面
        return redirect('posts:my_post')
    else:
        return HttpResponseForbidden("Invalid request method.")
    
# 获取帖子
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def upload_images(self, request, pk=None):
        post = self.get_object()
        files = request.FILES.getlist('images')
        for file in files:
            Image.objects.create(post=post, image=file)
        return Response({'status': 'images uploaded'})

# 获取图片
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 用户发送帖子
# class PostCreateAPIView(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)