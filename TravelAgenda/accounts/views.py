from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            #login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful!')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match!')

    return render(request, 'accounts/register.html')  

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
        print("hi")
        if user is not None:
            login(request, user)
            print("I am login")
            messages.success(request, 'Login successful!')
            return redirect('dashboard:dashboard') 
        else:
            print("user is not here")
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')