from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deploy_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    user = models.ForeignKey(
        "users.User",
        related_name="works",
        on_delete=models.CASCADE,
    )
