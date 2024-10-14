from django.shortcuts import render
from .models import Agenda
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
    return render(request, 'agenda/myagenda.html')