from django.urls import path
from .views import EmpresaAPIView

urlpatterns = [
    path('empresas/', EmpresaAPIView().as_view(), name='empresas'),
]