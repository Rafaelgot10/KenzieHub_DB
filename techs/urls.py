from django.urls import path
from .views import TechView, TechDetailView

urlpatterns = [
    path("techs/", TechView.as_view()),
    path("techs/<int:pk>/", TechDetailView.as_view()),
]
