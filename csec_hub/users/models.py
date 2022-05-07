from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class User(AbstractUser):
    
    SEXCHOICE = (
        ('M', 'Male'),
        ('F','Female'))
    
    def upload_to_profile(self, filename):
        return 'dev_score_board/%s' % filename


    telegram_username = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEXCHOICE)
    profile_picture = models.ImageField(upload_to_profile, null=True, blank=True)
    phone = models.CharField(max_length=13)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone']
    
    
class Memebership(User):
    school_id = models.CharField(max_length=255, blank=True, null=True)
    member_of = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='member_type')
    member_authority = models.ForeignKey('Authority', on_delete=models.CASCADE, null=True, blank=True, related_name='member_authority')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class Division(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    vacancy = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Authority(models.Model):
    position = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.position


    


