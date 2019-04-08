from django.urls import path
from . import views


urls = [
    path('status/<int:tweet_id>',
         views.StatusView.as_view(), name='status_detail'),
    path('tweet/<int:tweet_id>',
         views.StatusView.as_view(), name='tweet_detail'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('status/', views.CreateStatusView.as_view(), name='post_status'),
    path('tweet/', views.CreateStatusView.as_view(), name='tweet'),
]
