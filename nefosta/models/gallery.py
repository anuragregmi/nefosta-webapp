from django.db import models

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/', null=False)
    album_name = models.CharField(max_length=30)
