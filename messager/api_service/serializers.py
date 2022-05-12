from rest_framework import serializers
from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'user_id', 'message', 'status']


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['user_id', 'message']


