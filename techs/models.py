from django.db import models


class techsStatus(models.TextChoices):
    Iniciante = "Iniciante"
    Intermediário = "Intermediário"
    Avançado = "Avançado"


class Tech(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, choices=techsStatus.choices, default=techsStatus.Iniciante
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    user = models.ForeignKey(
        "users.User",
        related_name="techs",
        on_delete=models.CASCADE,
    )
