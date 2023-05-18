from django.core.signals import request_started, request_finished, got_request_exception
from django.contrib.auth.models import User
from django.dispatch import receiver


# TRIGGERED BEFORE REQUEST
# HERE sender = django.core.handlers.wsgi.WSGIHandler
@receiver(request_started)
def called_before_request(sender, environ, **kwargs):
    print("----------------------------------------")
    print("Before Request!")
    print("Sender : ", sender)
    print("User Instance : ", environ)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")

# TRIGGERED AFTER REQUEST
@receiver(request_finished)
def called_after_request(sender, **kwargs):
    print("----------------------------------------")
    print("After Request!")
    print("Sender : ", sender)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")

# At request Exception sender will be None