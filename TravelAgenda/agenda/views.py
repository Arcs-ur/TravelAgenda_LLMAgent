from django.shortcuts import render

def agenda_main(request):
    return render(request, 'agenda/main.html')

def agenda_calendar(request):
    return render(request, 'agenda/calendar.html')
