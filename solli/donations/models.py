from django.db import models

import core.models
from core.models import BaseEntry
from users.models import User


# Create your models here.

class Donation(BaseEntry):

    def __str__(self):
        return f"{self.title} (doação pertencente a {self.user.username if self.user else 'Usuário deletado'})"
