from django.db import models

from nefosta.models.abstract import BaseModel


class LinkCategory(BaseModel):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Link(BaseModel):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    link = models.URLField(blank=False)
    category = models.ForeignKey(
        LinkCategory, related_name="links",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
