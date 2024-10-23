from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser  # 引入自定义用户模型

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # 使用自定义用户模型
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为每个字段设置 placeholder 属性
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat password'})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        # 检查两次输入的密码是否一致
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        
        # 检查密码是否与用户名相同
        if password1 == self.cleaned_data.get('username'):
            raise ValidationError("Password cannot be the same as the username.")
        
        # 检查密码长度
        if len(password1) < 8:
            raise ValidationError("This password is too short. It must contain at least 8 characters.")
        
        # 检查密码是否包含数字
        if not any(char.isdigit() for char in password1):
            raise ValidationError("The password must contain at least one digit.")
        
        # 检查密码是否包含大写字母
        if not any(char.isupper() for char in password1):
            raise ValidationError("The password must contain at least one uppercase letter.")
        
        # 检查密码是否包含小写字母
        if not any(char.islower() for char in password1):
            raise ValidationError("The password must contain at least one lowercase letter.")
        
        return password2
