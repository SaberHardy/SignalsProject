from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from signalsApp.models import Post

request_counter_signal = Signal(['timestamp'])


def home(request):
    request_counter_signal.send(sender=Post, timestamp='2000-02-12')
    # print(request.POST.get('name', 'This is default value!!'))
    print(request.POST.get('name'))
    return render(request, 'signalApp/home.html')


"""
All of these methods are working perfectly but the problem is what
if i want to send messages or i want to apply some funcs after finishing tasks
"""


@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print("post request receiver finished!!!")


@receiver(request_counter_signal)
def post_request_counter_receiver(sender, **kwargs):
    # request_counter_signal.send(sender=Post, timestamp='2000/02/12')
    print(f"the time is {kwargs['timestamp']}")
