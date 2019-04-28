from django.db import models

from nefosta.models.abstract import BaseModel


class Career(BaseModel):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    link_to_site = models.URLField()

    def __str__(self):
        return f"{self.heading} - {self.link_to_site}"
