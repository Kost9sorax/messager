from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import StatusTypes


class MessagesApiList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class MessageApiCreate(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer


class MessageApiUpdate(generics.CreateAPIView):
    serializer_class = MessageUpdateSerializer
    queryset = Messages.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        message = get_object_or_404(Messages, pk=request.data.get('message_id'))
        message.status = StatusTypes.CORRECT.value if request.data.get('success') == 'True' else StatusTypes.BLOCKED.value
        message.save()
        return Response("ok")
