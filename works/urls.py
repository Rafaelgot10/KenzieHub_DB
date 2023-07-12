from django.urls import path
from .views import WorkView, WorkDetailView

urlpatterns = [
    path("works/", WorkView.as_view()),
    path("works/<int:pk>/", WorkDetailView.as_view()),
]
