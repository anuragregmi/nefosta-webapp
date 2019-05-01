from django.core.exceptions import ValidationError
from django.db import models

from nefosta.models.abstract import BaseModel


class DownloadCategory(BaseModel):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class DownloadResource(BaseModel):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(
        DownloadCategory,
        on_delete=models.CASCADE, related_name="downloads"
    )
    _url = models.URLField("URL", blank=True)
    file = models.FileField(null=True, blank=True)

    def save(self):
        if not(self._url or self.file):
            raise ValidationError("Either `url` or `file` must be set.")
        super().save()

    @property
    def url(self):
        if self.file:
            return self.file.url
        return self._url

    def __str__(self):
        return f"{self.title} - {self.category.title}"
