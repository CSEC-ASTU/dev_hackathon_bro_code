from django.db import models
from django.contrib.auth.models import AbstractUser


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
    
    
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='membership')
    school_id = models.CharField(max_length=255, blank=True, null=True)
    member_of = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='member_type', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_accepted = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.user.username

class Excuitive(models.Model):
    user = models.OneToOneField(Membership, on_delete=models.CASCADE)
    authority = models.OneToOneField('Authority', on_delete=models.CASCADE, null=True, blank=True, related_name='authority')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Excuitive'
        verbose_name_plural = 'Excuitives'
    
    def __str__(self):
        return 


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


    


