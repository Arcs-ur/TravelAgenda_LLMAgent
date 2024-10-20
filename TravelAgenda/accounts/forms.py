from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
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
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        
        # 检查密码是否与用户名相同
        if password1 == self.cleaned_data.get('username'):
            raise ValidationError("Password cannot be the same as the username.")
        
        # 检查密码长度
        if len(password1) < 8:
            raise ValidationError("This password is too short. It must contain at least 8 characters.And the password must contain digit, uppercase letter, lowercase letter")
        
        # 检查密码是否包含数字
        if not any(char.isdigit() for char in password1):
            raise ValidationError("This password must contain at least 8 characters.And the password must contain digit, uppercase letter, lowercase letter")
        
        # 检查密码是否包含大写字母
        if not any(char.isupper() for char in password1):
            raise ValidationError("This password must contain at least 8 characters.And the password must contain digit, uppercase letter, lowercase letter")
        
        # 检查密码是否包含小写字母
        if not any(char.islower() for char in password1):
            raise ValidationError("This password must contain at least 8 characters.And the password must contain digit, uppercase letter, lowercase letter")
        
        return password2