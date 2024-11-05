from .models import Notification


def unread_notification_count(request):
    if request.user.is_authenticated:
        return {
            'unread_count': Notification.objects.filter(user=request.user, is_read=False).count()
        }
    return {}
def message_processor(request):
    if request.user.is_authenticated:
        messages = Notification.objects.filter(user=request.user,is_read=False).order_by('-created_at')  # 获取所有消息
        return {'ms': messages}
    return {'ms': []}  # 未认证用户返回空列表
