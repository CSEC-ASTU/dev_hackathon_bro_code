from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Membership, Division


from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


User = get_user_model()

@receiver(post_save, sender=Membership)
def add_to_group(sender, instance, created, **kwargs):
   if created:
       new_group, created = Group.objects.get_or_create(name=instance.member_of.name)
       instance.groups.add(new_group)
       instance.save()
   else:
       pass




@receiver(pre_save, sender=Membership)
def vacancy_handler(sender, instance, **kwargs):
    # check if the member is already in registered
    if Membership.objects.filter(uuid=instance.uuid).exists():
        print("Existance of this bitch is real")
        pass
    else:
        print("hahaha rec bitch")
        division_count = Division.objects.filter(name=instance.member_of).count()
        division_vacancy = Division.objects.get(name=instance.member_of).vacancy
        print("max is reached man")
        if division_count < division_vacancy:
            instance.is_active = False
        else:
            raise ValidationError("max vacancy reached")
            # raise ValidationError(_(f'Max vacancy for {instance.member_of} divisio is {instance.member_of.vacancy}'), code='division_vacancy_limit_reached')






