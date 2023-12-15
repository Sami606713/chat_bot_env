from django.shortcuts import render
# from django import models
from bot.models import Conversation
from API.serilizer import ChatSerializer
from rest_framework import viewsets,permissions
# Create your views here.
class ChatViewSet(viewsets.ModelViewSet):
    queryset =Conversation.objects.all()
    serializer_class = ChatSerializer


