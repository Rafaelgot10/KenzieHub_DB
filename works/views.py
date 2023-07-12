from django.utils import timezone
from .models import Work
from .serializers import WorkSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class WorkView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        updated_at = timezone.now()
        created_at = timezone.now()
        print(user)
        serializer.save(
            updated_at=updated_at,
            created_at=created_at,
            user=user,
        )


class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def perform_update(self, serializer):
        updated_at = timezone.now()
        serializer.save(updated_at=updated_at)
