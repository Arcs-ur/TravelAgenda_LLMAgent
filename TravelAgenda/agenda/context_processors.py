from django.utils import timezone
from .models import AgendaLocation

def agenda_data(request):
    total_locations = AgendaLocation.objects.count()
    top_three_locations = AgendaLocation.objects.all()[:3]

    for location in top_three_locations:
        location.progress = calculate_progress(location)  # 计算进度

    return {
        'total_locations': total_locations,
        'top_three_locations': top_three_locations,
    }

def calculate_progress(location):
    now = timezone.now()
    if now < location.departure_time:
        return 0  # 任务尚未开始
    elif now > location.arrival_time:
        return 100  # 任务已完成
    else:
        # 计算任务进度
        total_duration = (location.arrival_time - location.departure_time).total_seconds()
        elapsed_time = (now - location.departure_time).total_seconds()
        return min(int((elapsed_time / total_duration) * 100), 100)  # 限制在0-100之间
