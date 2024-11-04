from django.db import models
from django.contrib.auth import get_user_model

class Notification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"