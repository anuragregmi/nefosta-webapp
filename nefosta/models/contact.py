from django.core.exceptions import ValidationError
from django.db import models

from nefosta.models.abstract import BaseModel


class Contact(BaseModel):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.address}-{self.phone_number}-{self.email_address}"

    def clean_fields(self, exclude=None):
        if Contact.objects.exists():
            raise ValidationError("Can not add more than one contact")
        return super().clean_fields(exclude=exclude)
