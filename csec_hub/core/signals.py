
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User
from .models import Feed, FeedType, Event
from .bot import send_to_subscribers
from django.core.mail import EmailMessage
from django.template.loader import render_to_string




@receiver(post_save, sender=Feed)
def send_feed_notification(sender, instance, created, **kwargs):
    feed = instance
    feed_type = feed.type
    subscribers = feed_type.subscribers.all()
    is_sent = feed.is_sent
    if created and is_sent==False:
        current_site = 'csechub.com'
        mail_subject = 'News Feed For You.'
            
        for subscriber in subscribers:
            message = render_to_string('feed_notification.html', {
                'user': user.username,
                'domain': current_site,
                'feed': feed,
                
                })
        
            to_email = instance.subscriber.email
            try:

                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                    )
                email.send()
                instance.is_sent = True
                instance.save()
            except Exception as e:
                print(e)
                pass
    elif is_sent==False:
        print(feed_type.subscribers.all(), '>>>>>>>>>>>>>>> No telegram username')
        for subscriber in feed_type.subscribers.all():
            print(subscriber.telegram_username,">>>>>>>>>>>>>>>>>>>>>")
            if subscriber.telegram_username:
                print(subscriber.telegram_username,">>>>>>>>>>>>>>>>>>>>> username")
                send_to_subscribers(instance.title)
                instance.save()
                break
            else:
                print('>>>>>>>>>>>>>>> No telegram username')
#             

        
@receiver(pre_save, sender=Feed)
def send_feed_notification(sender, instance, **kwargs):
    feed = instance
    feed_type = feed.type
    subscribers = feed_type.subscribers.all()
    if feed.is_sent==False:
        print(feed_type.subscribers.all(), '>>>>>>>>>>>>>>> No telegram username')
        for subscriber in feed_type.subscribers.all():
            print(subscriber.telegram_username,">>>>>>>>>>>>>>>>>>>>>")
            if subscriber.telegram_username:
                print(subscriber.telegram_username,">>>>>>>>>>>>>>>>>>>>> username")
                send_to_subscribers(instance.title)
                instance.save()
                break
            else:
                print('>>>>>>>>>>>>>>> No telegram username')
            
        current_site = 'csechub.com'
        mail_subject = 'News Feed For You.'

        for subscriber in subscribers:
            message = render_to_string('feed_notification.html', {
                        'user': subscriber.username,
                        'domain': current_site,
                        'feed': feed,
                        
                        })


            to_email = subscriber.email
            try:
                email = EmailMessage(
                mail_subject, message, to=[to_email]
                                )
                email.send()
            except Exception as e:
                print(e)    
                pass



    



                


