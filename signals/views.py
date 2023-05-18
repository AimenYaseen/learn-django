from django.shortcuts import render, HttpResponse
from .custom_signals import notification

# Create your views here.
def send_signal(request):
    notification.send(sender=None, request=request, user=['Abc', 'Def'])
    return HttpResponse("This is Django Custom Signal")