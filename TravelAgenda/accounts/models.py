from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return self.username
#这里的profile指的是用户的用户画像，包括手机号码、头像、用户名、密码会由abstractuser自动管理