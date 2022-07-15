from django.dispatch import Signal, receiver

notification = Signal()

@receiver(notification)
def accept_signal(sender, **kwargs):
    print("----------------------------------------")
    print("Custom Signal")
    print("Sender : ", sender)
    print("Kwargs : ", kwargs)