from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class modules(models.TextChoices):
    primeiro = "Primeiro módulo (Introdução ao Frontend)"
    segundo = "Segundo módulo (Frontend Avançado)"
    terceiro = "Terceiro módulo (Introdução ao Backend)"
    quarto = "Quarto módulo (Backend Avançado)"


def validate_min_length(value):
    if len(value) < 6:
        raise ValidationError("password: minimum is 6 characters")


class User(AbstractUser):
    username = models.CharField(unique=True, validators=[validate_min_length])
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    course_module = models.CharField(
        max_length=255,
        choices=modules.choices,
        default=modules.primeiro,
    )
    bio = models.CharField(max_length=255, null=True)
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    avatar_url = models.URLField(null=True)
