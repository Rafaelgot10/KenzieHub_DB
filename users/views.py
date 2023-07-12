from django.utils import timezone
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        updated_at = timezone.now()
        serializer.save(updated_at=updated_at)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
