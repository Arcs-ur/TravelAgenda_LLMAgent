from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 

from django.db.models import Q
from .serializers import PostSerializer, ImageSerializer
from .models import Post, Image
from .forms import PostForm

# 查看所有用户的帖子
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/post_list.html'  
    context_object_name = 'posts'  
    ordering = ['-created_at']  
    paginate_by = 4
    def get_queryset(self):
        queryset = super().get_queryset()
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
        form.instance.user = self.request.user
        self.object = form.save()
        
        # 上传图片
        images = self.request.FILES.getlist('images')
        for image in images:
            Image.objects.create(post=self.object, image=image)
        
        # 上传帖子成功到post_detail页面
        return redirect('posts:post_detail', pk=self.object.pk)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.pk})

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

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]