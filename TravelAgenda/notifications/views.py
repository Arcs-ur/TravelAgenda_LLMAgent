from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from .forms import NotificationForm
@login_required
def view_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/view_notifications.html', {'notifications': notifications})

from django.shortcuts import get_object_or_404, redirect

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications:view_notifications')
