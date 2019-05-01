from django.db import models

from nefosta.models.abstract import BaseModel


class Album(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Photo(BaseModel):
    photo = models.ImageField(upload_to='gallery/', null=False)
    album = models.ForeignKey(Album, related_name="photos",
                              on_delete=models.CASCADE)
    show_in_carousel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.album.name} - {self.photo.name}"
