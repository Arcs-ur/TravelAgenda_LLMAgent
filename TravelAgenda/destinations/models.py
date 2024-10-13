from django.db import models

# Create your models here.

# destination的model是包括了名字、地址、对应的一些标签（必吃、必住、必玩、必逛总计四种标签）、还有对应的跳转链接（可以在查询被返回一起返回方便用户点击）
class Destination(models.Model):
    TAG_CHOICES = [
        ('EAT', '必吃'),
        ('HOTEL', '必住'),
        ('PLAY', '必玩'),
        ('VISIT', '必逛'),
    ]

    name = models.CharField(max_length=100)  # 名字
    address = models.CharField(max_length=255)  # 地址
    tags = models.CharField(max_length=10, choices=TAG_CHOICES)  # 标签
    link = models.URLField(max_length=200, blank=True, null=True)  # 跳转链接

    def __str__(self):
        return self.name