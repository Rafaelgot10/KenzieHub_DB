from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "course_module",
            "password",
            "bio",
            "contact",
            "techs",
            "works",
            "created_at",
            "updated_at",
            "avatar_url",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
            "password": {"write_only": True},
            "techs": {"read_only": True},
            "works": {"read_only": True},
            "Created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        depth = 1

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(instance.password)
        serializer = UserSerializer(
            instance,
            data=validated_data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        instance.save()

        return instance


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]
