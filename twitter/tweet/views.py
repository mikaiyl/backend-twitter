from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from .models import Tweet
from .forms import CreateTweetForm

# Create your views here.


class StatusView(View):
    template_url = 'tweet/status_detail.html'

    def get(self, request, tweet_id):
        self.tweet = Tweet.objects.get(id=tweet_id)
        return render(request, self.template_url, {
            'tweet': self.tweet
        })


class FeedView(ListView, LoginRequiredMixin):
    template_name = 'tweet/status_list.html'
    queryset = Tweet.objects.order_by('-timestamp')[:10]
    context_object_name = 'status_feed'


class CreateStatusView(CreateView, LoginRequiredMixin):
    model = Tweet
    form_class = CreateTweetForm
    success_url = reverse_lazy('feed')
    template_name = 'tweet/status_create.html'
