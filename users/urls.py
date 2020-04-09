"""Users URLS.s"""

#Django
from django.urls import path

#views
from users import views

urlpatterns = [

    # Management
    path(
        route='/',
        view=views.HoliView.as_view(),
        name='signup'
    ),
]