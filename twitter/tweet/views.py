from django.shortcuts import render
from django.views import View, ListView
from .models import Tweet

# Create your views here.


class StatusView(View):
    template_url = 'tweet/status_list.html'

    def get(self, request, tweet_id):
        self.tweet = Tweet.objects.get(id=tweet_id)
        return render(request, self.template_url, {
            'tweet': self.tweet
        })


class FeedView(ListView):
    model = Tweet

