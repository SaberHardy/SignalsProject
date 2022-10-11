from django.shortcuts import render

from .models import Room


def index_view(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'djangoChannels/index.html', context=context)


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    context = {
        'room': chat_room,
    }
    return render(request, 'djangoChannels/room.html', context=context)
