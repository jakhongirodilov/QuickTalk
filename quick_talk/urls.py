from django.urls import path
from .views import home_page, profile_list, profile, post, LikeView
urlpatterns = [
    path("", home_page, name="home"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('post/<int:pk>/', post, name='post'),
    path('like/<int:pk>/', LikeView, name='like_post')
]