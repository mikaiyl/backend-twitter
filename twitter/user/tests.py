from django.test import TestCase
from . import models
import factory


# Create your tests here.
class TwitterUserFactory(factory.django.DjangoModelFactory):

    class Mete:
        model = models.TwitterUser

    username = factory.Faker('user_name')
    bio = factory.Faker('bio')

    @staticmethod
    def make_users(num):
        for n in range(num):
            user = TwitterUserFactory
            user.save()
            yield user


class UserTestCase(TestCase):

    def setUp(self):
        self.users = TwitterUserFactory.make_users(20)
