from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # 导入用户模型

class Location(models.Model):
    name = models.CharField(max_length=200)  # 地点名称
    address = models.CharField(max_length=300, blank=True)  # 地址（可选）
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Agenda(models.Model):
    title = models.CharField(max_length=200, default='Unnamed agenda')  # 日程名称
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键，指向用户模型

    def __str__(self):
        return f"{self.user.username}'s Agenda: {self.title}"

class AgendaLocation(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)  # 外键，指向日程
    departure_location = models.CharField(max_length=255)  # 出发地
    arrival_location = models.CharField(max_length=255)  # 目的地
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()  # 到达目的地的时间
    commute_info = models.TextField()  # 通勤信息
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.agenda.title}: {self.departure_location} to {self.arrival_location}"

    def calculate_progress(self):
        now = timezone.now()
        if now < self.departure_time:
            return 0  # 任务尚未开始
        elif now > self.arrival_time:
            return 100  # 任务已完成
        else:
            # 计算任务进度
            total_duration = (self.arrival_time - self.departure_time).total_seconds()
            elapsed_time = (now - self.departure_time).total_seconds()
            return min(int((elapsed_time / total_duration) * 100), 100)  # 限制在0-100之间
