from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title
