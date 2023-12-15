from  bot.models import Conversation
from rest_framework import serializers

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields =["user_input","response"]