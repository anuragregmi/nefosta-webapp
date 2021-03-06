import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from config.settings.base import STATIC_URL
from nefosta.models.abstract import BaseModel

User = get_user_model()


class Article(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()

    photo = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-posted_on', 'title')

    def __str__(self):
        return f"{self.title} - {self.author.username}"

    @property
    def photo_url(self):
        return self.photo.url if self.photo else \
            os.path.join(settings.STATIC_URL, 'img/default-article.jpg')
