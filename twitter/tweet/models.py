from django.db import models
from twitter.user.models import TwitterUser

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(
        TwitterUser, null=False,
        related_name='tweet_by_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=280)
    liked = models.ManyToManyField(
        TwitterUser, blank=True,
        related_name='liked_by')
    reply = models.BooleanField(default=False)
    thread = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.SET_NULL)
