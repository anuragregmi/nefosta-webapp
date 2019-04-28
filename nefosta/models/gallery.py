from django.db import models

from nefosta.models.abstract import BaseModel


class Album(BaseModel):
    name = models.CharField(max_length=150, unique=True)


class Photo(BaseModel):
    photo = models.ImageField(upload_to='gallery/', null=False)
    album_name = models.ForeignKey(Album, related_name="photos",
                                   on_delete=models.CASCADE)
