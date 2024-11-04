from django.urls import path
from .views import view_notifications, mark_as_read
app_name = 'notifications'
urlpatterns = [
    path('view/', view_notifications, name='view_notifications'),
    path('mark_as_read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
]
