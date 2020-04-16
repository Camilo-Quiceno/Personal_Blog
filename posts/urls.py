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
    path(
        route='feed/',
        view=views.FeedView.as_view(),
        name='feed'
    ),

    path(
        'newpost/', 
        views.NewPostView,
        name="newpost"
        ),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView, 
        name='postdetail'
    ),  
        
]