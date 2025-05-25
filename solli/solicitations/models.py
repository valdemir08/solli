from django.db import models
from core.models import BaseEntry
from users.models import User

class Solicitation(BaseEntry):

    def __str__(self):
        return f"{self.title} (pedido pertencente a {self.user.username if self.user else 'Usuário deletado'})"
