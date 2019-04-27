from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    photo = models.ImageField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
