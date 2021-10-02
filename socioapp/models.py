from django.db import models
import uuid
from datetime import datetime
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE )
    id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'profile_images/blank-profile-picture.png')
    bio = models.TextField(blank = True)
    firstname = models.CharField(max_length = 400)
    lastname = models.CharField(max_length = 400)
    location = models.CharField(max_length = 400)
    username = models.CharField(max_length = 400)
    def __str__(self):
        return self.username


class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    user = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'post_images')
    caption =models.TextField()
    created_at =models.DateTimeField(default = datetime.now)
    no_of_likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 500)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length = 500)
    user = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.user

        