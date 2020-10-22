from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework import status

class EmpresaAPIView(APIView):
    '''
    API de empresas
    '''

    def get(self,request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)