from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
<<<<<<< HEAD
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
=======
from .forms import CustomUserCreationForm  # 导入自定义表单
>>>>>>> b9419b7 (add password rules)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()  # 自动处理用户的创建和密码加密
            messages.success(request, 'Registration successful!')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})
=======
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
>>>>>>> b9419b7 (add password rules)

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(f"Attempting to authenticate user: {username}")

        # 检查用户是否存在
        try:
            user = User.objects.get(username=username)
            print(f"User found: {user.username}, Active: {user.is_active}")
        except User.DoesNotExist:
            print("User does not exist.")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request, 'Login successful!')
            return redirect('dashboard:dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')