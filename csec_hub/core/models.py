
from pyexpat import model
from django.db import models
from users.models import User, Membership, Division
from django.contrib.auth.models import Group
from taggit.managers import TaggableManager

class ScoreBoard(models.Model):

    def upload_to_score_board(self, filename):
        return 'cscore_board/%s' % filename

    title = models.CharField(max_length=255)
    body = models.TextField()
    posted_by = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='score_board_posted_by')
    tags = TaggableManager() 
    scoreboard_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    week = models.PositiveIntegerField()


class Feed(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.ForeignKey('FeedType', on_delete=models.CASCADE, related_name='feed_type')
    posted_by = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='feed_posted_by', limit_choices_to={'is_active': True},)
    tags = TaggableManager()
    is_sent = models.BooleanField(default=False)        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class FeedType(models.Model):
    name = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='feed_type')
    description = models.TextField()
    subscribers = models.ManyToManyField(User, related_name='subscribed_feed_type', limit_choices_to={'is_active': True}, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name.name

    
class Event(models.Model):
    def upload_to_event(self, filename):
        return f'event/%Y/%m/%d/{filename}'

    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to=upload_to_event, null=True, blank=True)    
    target = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='event_target')
    starting_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    posted_by = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='event_posted_by')
    tags = TaggableManager()
    has_form = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

# event partispant model
class EventParticipant(models.Model):
    def limit_choices_to_event_participant(self):
        return {'is_active': True}
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participant')
    participant = models.ManyToManyField(User, related_name='event_participant')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Subscription(models.Model):
   
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_subscription', limit_choices_to={'is_active': True},)
    tg_user_name = models.CharField(max_length=100)
    feed = models.ForeignKey(FeedType, on_delete=models.CASCADE, related_name='feed_subscription', limit_choices_to={'is_active': True},)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_subscription', limit_choices_to={'is_active': True},null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)



class Candidate(Membership):
    msg = models.TextField()
    votes = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.user.username


class Voting(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='voting_candidate')
    voted_by = models.ManyToManyField(User, related_name='candidate_voted')
    vote_date = models.DateTimeField()
    msg = models.CharField(max_length=3, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)