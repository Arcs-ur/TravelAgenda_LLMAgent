from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # 确保从你的模型中导入 CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    verification_code = forms.CharField(max_length=6, required=True, label="验证码", widget=forms.TextInput(attrs={'placeholder': '请输入验证码'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'verification_code']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为每个字段设置 placeholder 属性
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat password'})
        self.fields['verification_code'].widget.attrs.update({'placeholder': '请输入验证码'})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("此用户名已被注册。")
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("两次输入的密码不一致。")
        
        return password2
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        username = cleaned_data.get("username")
        
        if password and username and password == username:
            raise ValidationError("密码不能与用户名相同。")

        if password and len(password) < 8:
            raise ValidationError("密码长度过短，至少需要8个字符,且包含数字，大写字母，小写字母。")

        if password and not any(char.isdigit() for char in password):
            raise ValidationError("密码至少需要8个字符,且包含数字，大写字母，小写字母。")
        
        if password and not any(char.isupper() for char in password):
            raise ValidationError("密码至少需要8个字符,且包含数字，大写字母，小写字母。")
        
        if password and not any(char.islower() for char in password):
            raise ValidationError("密码至少需要8个字符,且包含数字，大写字母，小写字母。")

        return cleaned_data

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def clean_new_password(self):
        password = self.cleaned_data.get("new_password")

        if len(password) < 8:
            raise ValidationError("密码长度过短，至少需要8个字符，且包含数字，大写字母，小写字母。")

        if not any(char.isdigit() for char in password):
            raise ValidationError("密码至少需要8个字符,且包含数字，大写字母，小写字母。")

        if not any(char.isupper() for char in password):
            raise ValidationError("密码至少需要8个字符,且包含数字，大写字母，小写字母。")

        if not any(char.islower() for char in password):
            raise ValidationError("密码至少需要8个字符,且包含数字，大写字母，小写字母。")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("两次输入的密码不一致。")

        return cleaned_data