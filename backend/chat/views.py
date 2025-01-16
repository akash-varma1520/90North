from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Message

def index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/index.html', {'users': users})

def chat(request, user_id):
    other_user = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    )
    messages = messages.order_by('timestamp')
    return render(request, 'chat/chat.html', {'other_user': other_user, 'messages': messages})
