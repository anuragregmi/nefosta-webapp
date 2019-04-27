from django.core.exceptions import ValidationError
from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()

    def __str__():
        return f"{address}-{phone_number}-{email_address}"

    def clean_fields(self, exclude=None):
        if Contact.object.exists():
            raise ValidationError("Can not add more than one contact")
        return super().clean_fields(exclude=exclude)
