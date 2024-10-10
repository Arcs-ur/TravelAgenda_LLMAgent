from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'destinations'
urlpatterns = [
    path('', views.destination_main, name='main')
]
