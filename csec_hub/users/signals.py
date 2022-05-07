from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Membership


@receiver(post_save, sender=Membership)
def add_to_group(sender, instance, created, **kwargs):
   if created:
       new_group, created = Group.objects.get_or_create(name=instance.member_of.name)
       instance.user.groups.add(new_group)
       instance.save()
   else:
       pass










