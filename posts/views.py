"""Posts viesw's"""

#Django

from django.views.generic import  TemplateView
from django.contrib.auth import views as auth_views


#Models


class WelcomeView(TemplateView):
  
    template_name = 'posts/welcome.html'
    