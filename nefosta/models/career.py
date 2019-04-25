from django.db import models

class Career(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    link_to_site = models.URLField()
