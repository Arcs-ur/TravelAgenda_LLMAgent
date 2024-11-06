from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from agenda.models import AgendaLocation
from django.utils import timezone
from datetime import timedelta
@csrf_protect
@login_required
def dashboard(request):
    # 当前时间
    now = timezone.now() - timedelta(days=2)
    # 计算一周后的时间
    one_week_later = now + timedelta(days=7)

    # 获取一周内的 AgendaLocation 实例，并限制最多 20 条
    agendas = AgendaLocation.objects.filter(
        agenda__user=request.user,
        departure_time__lte=one_week_later,
        departure_time__gte=now
    ).order_by('-created_at')[:20]
    print(agendas)
    return render(request, 'dashboard.html', {'agendas': agendas})
