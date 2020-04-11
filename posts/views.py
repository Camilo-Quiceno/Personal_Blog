"""Posts viesw's"""

#Django

from django.views.generic import  TemplateView
from django.contrib.auth import views as auth_views
from django.shortcuts import render


#Models

class WelcomeView(TemplateView):
  
    template_name = 'posts/welcome.html'
    
class FeedView(TemplateView):
  
    template_name = 'posts/feed.html'


def NewPostView(request):

    return render(request, 'posts/newpost.html')