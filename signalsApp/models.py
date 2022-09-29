from django.db import models
from django.conf import settings
from django.db import models
from django.utils.text import slugify

from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
)

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        print(f"Send email to {instance.username}")
    else:
        print(f"The user has been saved-- {instance.username}")


# receiver function, sender
# post_save.connect(user_created_handler, sender=User)
