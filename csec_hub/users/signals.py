from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Authority, Membership, Excuitive

# Email Sender
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.core.mail import EmailMessage


@receiver(post_save, sender=Membership)
def add_to_group(sender, instance, created, **kwargs):
   if created:
       new_group, created = Group.objects.get_or_create(name=instance.member_of.name)
       instance.user.groups.add(new_group)
       instance.save()
   else:
       pass

@receiver(post_save, sender=Excuitive)
def accept_excutive(sender, instance, created, **kwargs):
    # send request to authority to accept excutive
    user = instance.user.user # get user
    if created:
        current_site = 'http://192.168.0.27:8000'
        mail_subject = 'Activate your blog account.'
        message = render_to_string('request_acceptance_email.html', {
        'user': user.username,
        'domain': current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        })
        to_email = instance.user.user.email
        # check if the email exits
        email = EmailMessage(
                mail_subject, message, to=[to_email]
        )
        email.send()
   






