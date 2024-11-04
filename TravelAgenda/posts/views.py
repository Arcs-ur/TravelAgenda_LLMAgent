from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponseRedirect,HttpResponseForbidden,JsonResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response

from django.views.generic import ListView,CreateView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin 

from django.db import transaction
from django.db.models import Q, Count, F

from .serializers import PostSerializer, ImageSerializer, PostSendSerializer
from .models import Post, Image, Comment
from .forms import PostForm,ImageForm,PostSendForm,CommentForm

from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory
from django import forms
# 查看所有用户的帖子
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/post_list.html'  
    context_object_name = 'posts'   
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        # 按照点赞的次数排序（热门度）
        queryset = queryset.annotate(num_likes=Count('likes')).order_by('-num_likes')
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
        queryset = Post.objects.filter(user=self.request.user).annotate(
            local_created_at=F('created_at')  # 或用Now()调整为本地时间
        ).order_by('-local_created_at')  # 按上海时间倒序排序
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return queryset
    
# 用户新增帖子
class PostSendView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostSendForm
    template_name = 'posts/send.html'
    
    def form_valid(self, form):
        serializer = PostSendSerializer(data={
            'title': form.cleaned_data['title'],
            'content': form.cleaned_data['content'],
            'images': self.request.FILES.getlist('images')
        })
        
        if serializer.is_valid():
            serializer.save(user=self.request.user) 
            return redirect('posts:my_post')
        return self.form_invalid(form, serializer.errors)
    
    def form_invalid(self, form, errors=None):
        context = self.get_context_data(form=form)
        if errors:
            print("Form errors:", form.errors)
            form.errors.update(errors)
        return self.render_to_response(context)
    
# 用户修改帖
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/edit.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:my_post')  # 默认保存成功后重定向的页面，可根据需求更改

    def get_context_data(self, **kwargs):
        # 获取上下文数据，将帖子表单和图片表单一起传递给模板
        data = super().get_context_data(**kwargs)

        # 获取现有图片数量
        existing_images_count = self.object.images.count()
        print(existing_images_count)
        # 动态设置 extra：如果已有9张图片，则不添加额外表单
        extra_forms = 0 if existing_images_count >= 9 else 1
        
        # 创建动态的 ImageFormSet
        ImageFormSet = inlineformset_factory(
            Post, Image, form=ImageForm, fields=['image'], extra=extra_forms, can_delete=True
        )

        #ImageFormSet = inlineformset_factory(Post, Image, form=ImageForm, fields=['image'], extra=1, can_delete=True)
        
        if self.request.POST:
            data['image_formset'] = ImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['image_formset'] = ImageFormSet(instance=self.object)
        
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']

        if form.is_valid() and image_formset.is_valid():
            # 保存帖子
            self.object = form.save()

            # 确保 formset 关联到正确的 Post 实例，并处理图片的增删改
            image_formset.instance = self.object
            image_formset.save()

            # 调试输出，查看 formset 是否正确处理了删除选项
            for form in image_formset:
                print(f"Image form: {form.cleaned_data}, to delete: {form.cleaned_data.get('DELETE', False)}")

            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


    def get_queryset(self):
        # 确保用户只能编辑自己的帖子
        return Post.objects.filter(user=self.request.user)
    
    def get_success_url(self) -> str:
        return super().get_success_url()

# 用户自己的帖子的详情展示页面
class MyPostDetailView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'posts/mypost_detail.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        return Comment.objects.filter(post=post, parent=None).order_by('-created_at')[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk']) 
        context['post'] = post  
        context['images'] = post.images.all() 
        return context
    
# 每个帖子的详情页视图
class PostDetailView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'posts/post_detail.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        # 筛选出最新的 20 条评论，并按倒序排列
        return Comment.objects.filter(post=post, parent=None).order_by('-created_at')[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])  # 获取帖子对象
        context['post'] = post  # 将帖子对象传递到模板
        context['images'] = post.images.all()  # 获取帖子相关的图片
        context['form'] = CommentForm()  # 评论表单
        return context

# 处理评论的视图
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['pk'])  # 获取相关的帖子对象
        form.instance.post = post  # 设置评论所属帖子
        form.instance.user = self.request.user  # 当前用户为评论作者

        # 如果是回复，设置父评论
        parent_id = self.request.POST.get('parent_id')
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)
            form.instance.parent = parent_comment

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.kwargs['pk']})
    
# 点赞功能
@login_required
@transaction.atomic
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = False

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': post.likes.count(),
    })

# 删除帖子
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 检查当前用户是否是发布者，防止其他用户删除帖子
    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    post.delete()
    return redirect(reverse('posts:my_post'))

# 批量删除帖子
@login_required
def batch_delete_posts(request):
    if request.method == 'POST':
        selected_post_ids = request.POST.get('selected_posts', '')
        if not selected_post_ids:
            messages.warning(request, 'No posts were selected for deletion.')
            return redirect('posts:my_post')
        selected_post_ids = selected_post_ids.split(',')
        posts_to_delete = Post.objects.filter(id__in=selected_post_ids, user=request.user)

        if posts_to_delete.exists():
            posts_to_delete.delete()
            messages.success(request, 'Selected posts deleted successfully!')
        else:
            messages.warning(request, 'No valid posts were found for deletion.')
        return redirect('posts:my_post')
    messages.error(request, 'Invalid request method.')
    return redirect('posts:my_post')
    
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

