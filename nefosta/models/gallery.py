from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Photo(models.Model):
    photo = models.ImageField(upload_to='gallery/', null=False)
    album_name = models.ForeignKey(Album, related_name="photos",
                                   on_delete=models.CASCADE)
