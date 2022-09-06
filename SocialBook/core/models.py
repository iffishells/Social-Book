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
        return  self.user.username
