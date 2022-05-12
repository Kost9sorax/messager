from rest_framework import serializers
from .models import *


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'user_id', 'message', 'status']


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['user_id', 'message']


class MessageUpdateSerializer(serializers.ModelSerializer):
    message_id = serializers.IntegerField()
    status = serializers.BooleanField(default=False)

    class Meta:
        model = Messages
        fields = ['message_id', 'status']
