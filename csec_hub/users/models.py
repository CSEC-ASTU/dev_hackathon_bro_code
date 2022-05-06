from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group



class User(AbstractUser):
    
    SEXCHOICE = (
        ('M', 'Male'),
        ('F','Female'))
    
    telegram_username = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEXCHOICE)
    profile_picture = models.ImageField(upload_to='')
    phone = models.CharField(max_length=13)
    
    
class Memebership(User):
    user_id = models.CharField(max_length=255, blank=True, null=True)
    member_of = models.ForeignKey('Division', on_delete=models.CASCADE, related_name='member_type')
    authority = models.ForeignKey('Authority', on_delete=models.CASCADE, null=True, blank=True, related_name='authority')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.username


    
    def add_to_group(self):
        new_group = Group.objects.get_or_create(name = self.memeber_of)
        self.groups.add(new_group)
        self.save()

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


    


