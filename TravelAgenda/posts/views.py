from django.shortcuts import render

def post_show(request):
    return render(request, 'posts/show.html')

def post_send(request):
    return render(request, 'posts/send.html')
