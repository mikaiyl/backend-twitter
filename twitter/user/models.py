from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TwitterUser(models.Model):
    # description of user.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    # avatar =
    # header =

    # Interactions with other users
    followers = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)
    blocked = models.ManyToManyField('self', blank=True)
