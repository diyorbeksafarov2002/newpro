from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name}"
