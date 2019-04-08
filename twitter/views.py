# from django.contrib.auth import authenticate, login
# from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View


class main(View):
    template_name = 'main.html'

    def get(self, request):
        response = TemplateResponse(request, self.template_name, {})
        return response
