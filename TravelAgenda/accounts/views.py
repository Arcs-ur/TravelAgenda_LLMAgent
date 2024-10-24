from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.cache import cache
from .forms import CustomUserCreationForm
from django.core.mail import send_mail  # 确保导入
import random
import string
from django.http import JsonResponse
import json

def send_verification_code(email):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    send_mail(
        '您的验证码',
        f'您的验证码是: {code}',
        'h1185038823@163.com',  # 发件人邮箱
        [email],
        fail_silently=False,
    )
    cache.set(email, code, timeout=300)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            verification_code = form.cleaned_data.get('verification_code')
            stored_code = cache.get(email)
            if verification_code == stored_code:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('accounts:login')
            else:
                messages.error(request, '验证码错误，请重新输入。')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def send_code_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            if email:
                send_verification_code(email)
                return JsonResponse({'message': '验证码已发送，请检查您的邮箱。'}, status=200)
            else:
                return JsonResponse({'error': '请输入有效的邮箱地址。'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': '无效请求。'}, status=400)
    return JsonResponse({'error': '无效请求。'}, status=400)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard:dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')
