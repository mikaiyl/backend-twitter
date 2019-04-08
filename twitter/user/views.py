from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User, TwitterUser


# Create your views here.

class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        self.user = form.save()
        TwitterUser.objects.create(
            user=User.objects.filter(username=self.user).first())
        return super().form_valid(form)


class DetailView():
    pass
