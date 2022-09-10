import uuid
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


# model for profile data
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.CharField(max_length=500, blank=True)
    # will media app for handling the image data
    profile_img = models.ImageField(upload_to='Profile_images', default='blank-profile.png')
    location = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_like = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_image')

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class FollowerCount(models.Model):
    # follower model for each user
    follower = models.CharField(max_length=500)
    username = models.CharField(max_length=500)

    def __str__(self):
        return self.username
