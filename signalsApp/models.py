from django.db import models
from django.conf import settings
from django.db import models
from django.utils.text import slugify

from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,  # does not have a created variable
    post_save,
)

User = settings.AUTH_USER_MODEL


@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    before saved into database
    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
    print(f"Send email to {instance.username} - {instance.id}")


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    After saved into database
    :param sender:
    :param instance:
    :param created:
    :param args:
    :param kwargs:
    :return:
    """
    if created:
        instance.save()
        print(f"Send email to {instance.username}")
        # We need to add a saved method to save the instance
    else:
        print(f"The user has been saved-- {instance.username} ==> {instance.id}")


# receiver function, sender
pre_save.connect(user_pre_save_receiver, sender=User)
