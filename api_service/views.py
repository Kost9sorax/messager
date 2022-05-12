from django.shortcuts import render
from rest_framework import generics
from .models import Messages
from .serializers import MessagesSerializer, MessageCreateSerializer


class MessagesApiList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class MessageApiCreate(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer
