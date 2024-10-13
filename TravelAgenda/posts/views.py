from django.shortcuts import render,redirect,get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, Image
from .serializers import PostSerializer, ImageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Post

# 查看所有用户的帖子
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/post_list.html'  
    context_object_name = 'posts'  
    ordering = ['-created_at']  
    paginate_by = 10  



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    images = post.images.all()
    return render(request, 'posts/post_detail.html', {'post': post, 'images': images})

from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('posts:post_detail', args=[str(pk)]))

@login_required
def post_send(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        images = request.FILES.getlist('images')

        post = Post.objects.create(user=request.user, title=title, content=content)

        for image in images:
            Image.objects.create(post=post, image=image)

        return redirect('posts:post_detail', pk=post.pk)
    else:
        return render(request, 'posts/send.html')

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