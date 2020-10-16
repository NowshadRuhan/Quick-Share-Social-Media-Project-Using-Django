from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_profile')
    user_full_name = models.CharField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    dob = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=200,blank=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

class Follow(models.Model):
    follower = models.ForeignKey(User,  on_delete = models.CASCADE, related_name = 'follower')
    following = models.ForeignKey(User,  on_delete = models.CASCADE, related_name = 'following')
    created_date = models.DateTimeField(auto_now_add = True)
