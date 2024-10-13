from django.db import models

# Create your models here.
#agenda的database里面要包括日程的名字比如“2024北京行”，要包括日程的内容。
class agenda(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.name