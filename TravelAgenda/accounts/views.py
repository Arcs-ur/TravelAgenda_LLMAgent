from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm  # 导入自定义表单

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # 注册后自动登录
            messages.success(request, 'Registration successful!')
            return redirect('accounts:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(f"Attempting to authenticate user: {username}")

        # 检查用户是否存在
        try:
            user = CustomUser.objects.get(username=username)
            print(f"User found: {user.username}, Active: {user.is_active}")
        except CustomUser.DoesNotExist:
            print("User does not exist.")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request, 'Login successful!')
            return redirect('dashboard:dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')