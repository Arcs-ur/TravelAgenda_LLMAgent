from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'posts'
urlpatterns = [
    path('', views.post_show, name='show'),
    path('send', views.post_send, name='send'),
]
