from django.shortcuts import render
from .models import Agenda, AgendaLocation
from django.shortcuts import redirect,get_object_or_404
from .forms import *
from datetime import datetime
from datetime import timedelta
import json
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# def agenda_main(request):
#     return render(request, 'agenda/main.html')

def agenda_main(request):
    agendas = Agenda.objects.all()  # 获取所有 Agenda 实例
    return render(request, 'agenda/main.html', {'agendas': agendas})

def agenda_calendar(request):
    return render(request, 'agenda/calendar.html')

def agenda_map(request):
    return render(request, 'agenda/map.html')

def agenda_LLM(request):
    return render(request, 'agenda/LLM.html')

def agenda_my(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda/myagenda.html', {'agendas': agendas})

def agenda_list(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda/agenda_list.html', {'agendas': agendas})

def delete_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    agenda.delete()
    return redirect('agenda:agenda_list')

def delete_agendalocation(request, id):
    loc = get_object_or_404(AgendaLocation, id=id)
    loc.delete()
    return redirect('agenda:agenda_list')
# def update_agenda(request, id):
#     agenda = get_object_or_404(Agenda, id=id)
#     if request.method == 'POST':
#         agenda_form = AgendaForm(request.POST, instance=agenda)
#         # 这里可以处理 AgendaLocation 的更新
#         if agenda_form.is_valid():
#             agenda_form.save()
#             return redirect('agenda:agenda_list')
#     else:
#         agenda_form = AgendaForm(instance=agenda)

#     return redirect('agenda:agenda_list')
    # 处理更新逻辑（例如，显示表单并保存数据）
def update_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    if request.method == 'POST':
        agenda_form = TravelAgendaForm(request.POST, instance=agenda)
        if agenda_form.is_valid():
            agenda_form.save()
            return redirect('agenda:agenda_list')  # 更新后重定向到日程列表页面
    else:
        agenda_form = AgendaForm(instance=agenda)
    
    # 动态渲染更新页面，传递 Agenda 数据到模板
    return render(request, 'agenda/update_Travelagenda.html', {
        'agenda_form': agenda_form,
        'agenda': agenda,  # 传递当前日程对象
    })

def update_agendalocation(request,id):
    loc = get_object_or_404(AgendaLocation, id=id)  # 获取 AgendaLocation 对象
    agenda = loc.agenda
    if request.method == 'POST':
        agenda_form = AgendaForm(request.POST, instance=loc)  # 使用 AgendaLocationForm
        if agenda_form.is_valid():
            agenda_form.save()
            return redirect('agenda:agenda_list')  # 更新后重定向到日程列表页面
    else:
        agenda_form = AgendaLocationForm(instance=loc)  # 传递当前 AgendaLocation 实例
    
    # 动态渲染更新页面，传递 AgendaLocation 数据到模板
    return render(request, 'agenda/update_agenda.html', {
        'agenda_form': agenda_form,
        'location': loc,  # 传递当前 AgendaLocation 对象
    })


def add_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:agenda_list')  # 添加后重定向回日程列表
    else:
        form = AgendaForm()
    return render(request, 'agenda/add_agenda.html', {'form': form})

def add_Travelagenda(request):
    if request.method == 'POST':
        form = TravelAgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:agenda_list')  # 添加后重定向回日程列表
    else:
        form = TravelAgendaForm()
    return render(request, 'agenda/add_Travelagenda.html', {'form': form})

def calendar_view(request):
    # 获取所有的 Agenda 相关数据
    agendalocations = AgendaLocation.objects.all()
    # 构建 FullCalendar 所需的事件数据
    events = []
    for agendalocation in agendalocations:
        events.append(({
            "title":f"{agendalocation.departure_location.name} - {agendalocation.arrival_location.name}",
            "start":agendalocation.departure_time.isoformat(),
            "end":agendalocation.arrival_time.isoformat(),  # 事件结束时间, 假设为到达时间2小时后
            "departure_location":agendalocation.departure_location.name,
            "arrive_location":agendalocation.arrival_location.name,
            "transportation":agendalocation.commute_info,
            }
        ))
    events_json = json.dumps(events)
    context = {
        'events': events_json
    }
    return render(request, 'agenda/calendar.html', context)

class AgendaListView(LoginRequiredMixin, ListView):
    model = Agenda
    #model = Agenda
    template_name = 'agenda/agenda_list.html'
    context_object_name = 'agendas'
    ordering = ['-created_at']  # 根据创建时间排序
    paginate_by = 10  # 每页 10 条记录
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query = self.request.GET.get('q')
    #     if query:
    #         #queryset = queryset.filter(Q(title__icontains=query))
    #         queryset = queryset.filter(Q(departure_location__name__icontains=query)|Q(arrival_location__name__icontains=query)|Q(agenda__title__icontains=query))
    #     return queryset.values('agenda')
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
    
        if query:
        # 筛选出符合条件的 AgendaLocation 实例
            # filtered_locations = queryset.filter(
            #     Q(departure_location__name__icontains=query) |
            #     Q(arrival_location__name__icontains=query) |
            #     Q(agenda__title__icontains=query)|
            #     Q(commute_info__icontains=query)
            # )   
            queryset = queryset.filter(Q(title__icontains=query))
        # 获取这些实例对应的 agenda，并去重
            #agendas = filtered_locations.values('agenda').distinct()

        # 返回符合条件的 agenda
            return queryset