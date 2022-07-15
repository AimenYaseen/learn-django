from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

# USER LOGGED IN SUCCESSFULLY
@receiver(user_logged_in, sender=User)
def login_successful(sender, request, user, **kwargs):
    print("----------------------------------------")
    print("Login Successful!")
    print("Sender : ", sender)
    print("Request : ", request)
    print("User : ", user)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")

# Connect the signal user_logged_in.connect(receiver, sender)
# user_logged_in.connect(login_successful, sender=User)

# USER LOGIN FAILED
@receiver(user_login_failed)
def login_fail(sender, request, credentials, **kwargs):
    print("----------------------------------------")
    print("Login Fail!")
    print("Sender : ", sender)
    print("Request : ", request)
    print("Credentials : ", credentials)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")

# USER LOGGED OUT SUCCESSFULLY
@receiver(user_logged_out, sender=User)
def logout_successful(sender, request, user, **kwargs):
    print("----------------------------------------")
    print("Logout Successful!")
    print("Sender : ", sender)
    print("Request : ", request)
    print("User : ", user)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")
