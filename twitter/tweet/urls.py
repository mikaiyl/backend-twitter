from django.urls import path
from . import views


urls = [
    path('status/<int:tweet_id>',
         views.StatusView.as_view(), name='status_detail')
]
