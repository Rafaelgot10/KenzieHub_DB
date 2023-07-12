from rest_framework import serializers
from .models import Tech


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = [
            "id",
            "title",
            "status",
            "created_at",
            "updated_at",
            # "user",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            # "user": {"read_only": True},
        }
        depth = 1
