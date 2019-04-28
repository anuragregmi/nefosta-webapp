from django.db import models

from nefosta.models.abstract import BaseModel


class Publication(BaseModel):
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title
