from django.urls import path, include
from . import views


urls = [
    path('join/', views.CreateUserView.as_view(), name='new_user'),
]
