from django.db import models

# Create your models here.
#agenda的database里面要包括日程的名字比如“2024北京行”，要包括日程中涉及的地点、到达地点的时间、地点与地点之间的通勤。

class Location(models.Model):
    name = models.CharField(max_length=200)  # 地点名称
    address = models.CharField(max_length=300, blank=True)  # 地址（可选）

    def __str__(self):
        return self.name

class Agenda(models.Model):
    title = models.CharField(max_length=200,default='Unnamed agenda')  # 日程名称
    locations = models.ManyToManyField(Location, through='AgendaLocation',through_fields=('agenda', 'arrival_location'))  # 通过中间模型关联地点
    

    def __str__(self):
        return self.title

class AgendaLocation(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)  # 外键，指向日程
    departure_location = models.ForeignKey(Location, related_name='departure_locations', on_delete=models.CASCADE)  # 出发地
    arrival_location = models.ForeignKey(Location, related_name='arrival_locations', on_delete=models.CASCADE)  # 目的地
    arrival_time = models.DateTimeField()  # 到达目的地的时间
    commute_info = models.TextField()  # 通勤信息

    class Meta:
        unique_together = ('agenda', 'departure_location', 'arrival_location')  # 确保组合唯一

    def __str__(self):
        return f"{self.agenda.title}: {self.departure_location.name} to {self.arrival_location.name}"