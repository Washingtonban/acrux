from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Evento
from .serializers import EventoSerializer
from rest_framework import status


class EventoAPIView(APIView):
    '''
    API de eventos
    '''


    def get(self, request):
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
