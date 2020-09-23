from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework import status


class PessoaAPIView(APIView):
    '''
    API de pessoas
    :return:
    '''
    def get(self, request):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PessoaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)