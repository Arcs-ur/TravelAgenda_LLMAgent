from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'agenda'
urlpatterns = [
    path('', views.agenda_main, name='main'),
    path('calendar', views.agenda_calendar, name='calendar')
]
