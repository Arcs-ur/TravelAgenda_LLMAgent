from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

app_name = 'posts'
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    path('list', views.PostListView.as_view(), name='post_list'),
    path('mypost', views.MyPostListView.as_view(), name='my_post'),
    path('send', views.PostSendView.as_view(), name='send'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('posts/batch-delete/', views.batch_delete_posts, name='batch_delete_posts'),
    path('', include(router.urls)),
]