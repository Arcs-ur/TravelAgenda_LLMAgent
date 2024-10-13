from django.db import models
#这部分的需求是面向对象记录，对象是帖子，数据库的内容要包括：1.帖子的发布者，2.帖子的内容，3，帖子的发布时间，4.帖子的点赞数
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 发布者
    content = models.TextField()  # 帖子的内容
    created_at = models.DateTimeField(auto_now_add=True)  # 帖子的发布时间
    likes = models.PositiveIntegerField(default=0)  # 帖子的点赞数

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"
