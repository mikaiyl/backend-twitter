from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View


class main(View):
    template_name = 'main.html'

    def get(self, request):
        response = TemplateResponse(request, self.template_name, {})
        return response

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            redirect('signup')


class Login(View):
    template_name = 'main.html'

    def get(self, request):
        response = TemplateResponse(request, self.template_name, {})
        return response

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            redirect('signup')


class Signup(View):
    template_name = 'main.html'

    def get(self, request):
        response = TemplateResponse(request, self.template_name, {})
        return response

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            redirect('signup')
