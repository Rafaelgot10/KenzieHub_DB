from django.utils import timezone
from .models import Tech
from .serializers import TechSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class TechView(generics.ListCreateAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        updated_at = timezone.now()
        created_at = timezone.now()
        serializer.save(
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )


class TechDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer

    def perform_update(self, serializer):
        updated_at = timezone.now()
        serializer.save(updated_at=updated_at)
