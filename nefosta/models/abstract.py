from django.db import models


class BaseModel(models.Model):
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-posted_on',)
        abstract = True
