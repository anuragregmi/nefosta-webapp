from django.db import models

class Contact(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
