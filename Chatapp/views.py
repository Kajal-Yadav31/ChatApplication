from django.shortcuts import render,  redirect, get_object_or_404
from .models import ChatRoom, ChatMessage
from django.http import HttpResponseServerError
# Create your views here.


def index(request):
    chatrooms = ChatRoom.objects.all()

    return render(request, 'Chatapp/index.html', {'chatrooms': chatrooms})


def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]

    return render(request, 'Chatapp/room.html', {'chatroom': chatroom, 'messages': messages})
