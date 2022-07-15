from django.db.models.signals import pre_save, pre_init, pre_delete, post_save, post_init, post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver

# TRIGGERED BEFORE SAVING USER
@receiver(pre_save, sender=User)
def called_before_save(sender, instance, **kwargs):
    print("----------------------------------------")
    print("Pre_Save!")
    print("Sender : ", sender)
    print("User Instance : ", instance)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")

# Connect the signal user_logged_in.connect(receiver, sender)
# pre_save.connect(called_before_save, sender=User)

# TRIGGERED AFTER SAVING USER
@receiver(post_save, sender=User)
def called_after_save(sender, instance, created, **kwargs):
    print("----------------------------------------")
    print("POST SAVE!")
    print("Sender : ", sender)
    print("New User Created or not : ", created)
    print("User Instance : ", instance)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")


# TRIGGERED BEFORE INIT
@receiver(pre_init, sender=User)
def called_before_init(sender, *args, **kwargs):
    print("----------------------------------------")
    print("Pre_init!")
    print("Sender : ", sender)
    print("User Instance args: ", args)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")

# Connect the signal user_logged_in.connect(receiver, sender)
# pre_save.connect(called_before_save, sender=User)

# TRIGGERED AFTER INIT
@receiver(post_init, sender=User)
def called_after_init(sender, *args, **kwargs):
    print("----------------------------------------")
    print("POST INIT!")
    print("Sender : ", sender)
    print("Args : ", args)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")


# TRIGGERED BEFORE DELETING USER
@receiver(pre_delete, sender=User)
def called_before_delete(sender, instance, **kwargs):
    print("----------------------------------------")
    print("Pre_Delete!")
    print("Sender : ", sender)
    print("User Instance to be deleted : ", instance)
    print("keyword Arguments : ", kwargs)
    print("----------------------------------------")
