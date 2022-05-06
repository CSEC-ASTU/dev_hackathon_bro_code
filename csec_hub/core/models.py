from operator import mod
from django.db import models
from users.models import Memebership
from users.models import Division

class CpdScorBoard(models.Model):

    def upload_to_cpd_score_board(self, filename):
        return 'cpd_score_board/%s' % filename
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to_cpd_score_board)
    posted_by = models.ForeignKey(Memebership, on_delete=models.CASCADE, related_name='posted_by')
    tag = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class DevScoreBoard(models.Model):
    def upload_to_dev_score_board(self, filename):
        return 'dev_score_board/%s' % filename
        
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to_dev_score_board)
    tag = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Feed(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.ForeignKey('FeedType', on_delete=models.CASCADE, related_name='feed_type')
    posted_by = models.ForeignKey(Memebership, on_delete=models.CASCADE, related_name='posted_by')
    tag = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class FeedType(models.Model):
    name = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='feed_type')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name