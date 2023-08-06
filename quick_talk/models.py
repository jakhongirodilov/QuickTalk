from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django_project import settings


class Post(models.Model):
    user = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return f"{self.user.username}: {self.body[:30]}"
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='author_comments',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")
    