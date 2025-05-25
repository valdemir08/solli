from django.db import models

from users.models import User


# Create your models here.

class Campaign(models.Model):
    company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (campanha pertencente a {self.company.username if self.company else 'Usuário deletado'})"

