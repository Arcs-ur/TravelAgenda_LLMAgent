from django.shortcuts import render

def destination_main(request):
    return render(request, 'dashboard.html')
