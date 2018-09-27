from django.db import models
# Importar desde la app `auth` de django la clase AbstractUser
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Clase personalizada de usuarios
    age = models.PositiveIntegerField(
        verbose_name='Edad', default=0
    )