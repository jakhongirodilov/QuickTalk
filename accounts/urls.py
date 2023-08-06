from django.urls import path
from .views import signup_view, profile_edit

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('profile_edit/<int:pk>/', profile_edit, name='profile_edit')
]


