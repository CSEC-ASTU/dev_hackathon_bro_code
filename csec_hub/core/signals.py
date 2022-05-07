from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import FeedType


@receiver(post_save, sender=FeedType)
def add_to_group(sender, instance, created, **kwargs):
    if created:
        new_group, created = Group.objects.get_or_create(name=instance.name)
        User.groups.add(new_group)
        instance.save()
    else:
        pass

