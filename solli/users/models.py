from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_company = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.email:
            self.username = self.email
        else:
            raise ValueError("Email obrigatório para definir o username")
        super().save(*args, **kwargs)
