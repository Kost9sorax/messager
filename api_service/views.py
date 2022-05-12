from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import BasketTypes


class MessagesApiList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class MessageApiCreate(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer


class MessageApiUpdate(generics.CreateAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Messages.objects.all()

    def post(self, request):
        message = Messages.objects.get(pk=request.data['message_id'])
        message.status = BasketTypes.CORRECT.value if request.data.get("status") else BasketTypes.BLOCKED.name
        message.save()
        return Response("ok")
