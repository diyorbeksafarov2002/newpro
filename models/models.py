from django.db import models

class Contact(models.Model):
    class Call_type(models.TextChoices):
        Boglanildi = "Bog'lanildi"
        Boglanilmadi = "Bog'lanilmadi"
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)
    called = models.CharField(max_length=100, choices=Call_type, default=Call_type.Boglanilmadi)

    def __str__(self):
        return f"{self.name}    {self.called}"