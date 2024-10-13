from django.shortcuts import render

def agenda_main(request):
    return render(request, 'agenda/main.html')

def agenda_calendar(request):
    return render(request, 'agenda/calendar.html')

def agenda_map(request):
    return render(request, 'agenda/map.html')

def agenda_LLM(request):
    return render(request, 'agenda/LLM.html')

def agenda_my(request):
    return render(request, 'agenda/myagenda.html')