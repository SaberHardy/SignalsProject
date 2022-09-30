from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,  # does not have a created variable
    post_save,
)

User = settings.AUTH_USER_MODEL


# @receiver(pre_save, sender=User)
# def user_pre_save_receiver(sender, instance, *args, **kwargs):
#     """
#     before saved into database
#     :param sender:
#     :param instance:
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     print(f"Send email to {instance.username} - {instance.id}")
#
#
# @receiver(post_save, sender=User)
# def user_post_save_receiver(sender, instance, created, *args, **kwargs):
#     """
#     After saved into database
#     :param sender:
#     :param instance:
#     :param created:
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     if created:
#         instance.save()
#         print(f"Send email to {instance.username}")
#         # We need to add a saved method to save the instance
#     else:
#         print(f"The user has been saved-- {instance.username} ==> {instance.id}")


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Its working perfectly with this function,
# but it needed to avoid the instance.save()
# @receiver(post_save, sender=Post)
# def post_post_save(sender, instance, created, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)  # => this is ==> this-is
#         instance.save()

@receiver(pre_save, sender=Post)
def post_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)  # => this is ==> this-is


@receiver(pre_save, sender=Post)
def post_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)  # => this is ==> this-is
        # instance.save()
        if instance.id and instance.notify_users:
            instance.notify_users = False
            instance.notify_users_timestamp = timezone.now()
            print("Notified user")


# receiver function, sender
pre_save.connect(post_pre_save, sender=User)
