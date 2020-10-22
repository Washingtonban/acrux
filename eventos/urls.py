from django.urls import path
from .views import EventoAPIView

urlpatterns = [
    path('eventos/', EventoAPIView().as_view(), name='eventos'),
]