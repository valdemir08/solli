from django.db import models

from users.models import User


# Create your models here.
class BaseEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseProposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True