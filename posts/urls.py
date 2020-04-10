"""Posts URLS.s"""

#Django
from django.urls import path

#views
from posts import views

urlpatterns = [

    # Management
    path(
        route='',
        view=views.WelcomeView.as_view(),
        name='welcome'
    ),
]