"""Users URLS.s"""

#Django
from django.shortcuts import render
from django.views.generic import  TemplateView

#views

class HoliView(TemplateView):
    """Users sign up view"""

    template_name = 'users/holi.html'
    