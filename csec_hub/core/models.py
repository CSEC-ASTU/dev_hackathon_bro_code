

from django.db import models
from users.models import Membership
from users.models import Division
from django.contrib.auth.models import Group
from taggit.managers import TaggableManager

class ScoreBoard(models.Model):

    def upload_to_score_board(self, filename):
        return 'cscore_board/%s' % filename

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to_score_board)
    posted_by = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='score_board_posted_by')
    tags = TaggableManager() 
    scoreboard_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Feed(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.ForeignKey('FeedType', on_delete=models.CASCADE, related_name='feed_type')
    posted_by = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name='feed_posted_by')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class FeedType(models.Model):
    name = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='feed_type')
    description = models.TextField()
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
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title

     