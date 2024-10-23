from django.db import models
#这部分的需求是面向对象记录，对象是帖子，数据库的内容要包括：1.帖子的发布者，2.帖子的标题与内容，3，帖子的发布时间，4.帖子的点赞数 5.外键帖子的图片
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 发布者
    title = models.TextField() # 帖子的标题
    content = models.TextField()  # 帖子的内容
    created_at = models.DateTimeField(auto_now_add=True)  # 帖子的发布时间
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)  # Users who liked the post

    def total_likes(self):
        return self.likes.count()
    #likes = models.PositiveIntegerField(default=0)  # 帖子的点赞数

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)  # 关联到Post
    image = models.ImageField(upload_to='post_images/')  # 上传的图片文件
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 图片的上传时间

    def __str__(self):
        return f"Image for post {self.post.id} uploaded at {self.uploaded_at}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # 关联到Post
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 评论的用户
    content = models.TextField(max_length=100)  # 评论的内容
    created_at = models.DateTimeField(auto_now_add=True)  # 评论的创建时间
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)  # 父评论（用于回复）

    def __str__(self):
        if self.parent:
            return f"Reply by {self.user.username} on comment {self.parent.id}"
        return f"Comment by {self.user.username} on post {self.post.id}"