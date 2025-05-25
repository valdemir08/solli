from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    DOCUMENT_TYPES = [
        ("CPF", "Pessoa Física"),
        ("CNPJ", "Pessoa Jurídica")
    ]
    full_name = models.CharField(max_length=255)
    document = models.CharField(max_length=20, unique=True)
    document_type = models.CharField(max_length=4, choices=DOCUMENT_TYPES)
    is_company = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.email:
            self.username = self.email
        else:
            raise ValueError("Email obrigatório para definir o username")
        super().save(*args, **kwargs)
