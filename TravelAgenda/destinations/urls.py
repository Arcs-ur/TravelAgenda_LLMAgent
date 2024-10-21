from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'destinations'
urlpatterns = [
    path('', views.destination_main, name='main'),
    path('hotel', views.destination_hotel, name='hotel'),
    path('restaurant', views.destination_restaurant, name='restaurant'),
    path('shop', views.destination_shop, name='shop'),
    path('attraction/', views.destination_attraction, name='attraction'),
    path('traffic', views.destination_traffic, name='traffic'),
]
