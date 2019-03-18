from django.db import models

# Create your models here.


class Notify(models.Model):
    ACTION_CHOICES = (
        ('F', 'New Follower'),
        ('L', 'Like'),
        ('R', 'New Reply'),
    )

    from_user = models.ForeignKey(
        'user.TwitterUser', null=False,
        related_name='from_user', on_delete=models.CASCADE)
    notify_user = models.ForeignKey(
        'user.TwitterUser', null=False,
        related_name='to_ser', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=1, choices=ACTION_CHOICES)
    ref_tweet = models.ForeignKey(
        'tweet.Tweet', null=True, on_delete=models.CASCADE)
