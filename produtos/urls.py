from django.urls import path
from .views import ProdutoAPIView

urlpatterns = [
    path('produtos/', ProdutoAPIView().as_view(), name='produtos'),
]