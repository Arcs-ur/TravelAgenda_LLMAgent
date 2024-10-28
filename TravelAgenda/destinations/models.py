from django.db import models

# Create your models here.

# destination的model是包括了名字、地址、对应的一些标签（必吃、必住、必玩、必逛总计四种标签）、还有对应的跳转链接（可以在查询被返回一起返回方便用户点击）
from django.db import models

class Destination(models.Model):
    TAG_CHOICES = [
        ('EAT', '必吃'),
        ('HOTEL', '必住'),
        ('PLAY', '必玩'),
        ('VISIT', '必逛'),
    ]
    PLAY_TYPE_CHOICES = [
        ('FAMILY', '亲子路线'),          # Family-friendly route
        ('CITYSCAPE', '城市景观'),        # Cityscape
        ('NATURE', '自然景观'),          # Natural landscape
        ('CULTURE', '历史人文'),         # Historical and cultural sight
        ('ADVENTURE', '冒险探索'),       # Adventure
        ('SPORTS', '运动休闲'),          # Sports and recreation
    ]

    name = models.CharField(max_length=20)  # 名字
    address = models.CharField(max_length=255)  # 地址
    tags = models.CharField(max_length=10, choices=TAG_CHOICES)  # 标签
    link = models.URLField(max_length=200, blank=True, null=True)  # 跳转链接
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)  # 图片
    introduction = models.TextField(blank=True)  # 简介
    stars = models.IntegerField(default=5)  # 星级评分，5.0满分
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # 价钱
    play_type = models.CharField(
        max_length=15, 
        choices=PLAY_TYPE_CHOICES, 
        blank=True, 
        null=True, 
        help_text="仅适用于必玩标签"
    )  
    def __str__(self):
        return self.name
