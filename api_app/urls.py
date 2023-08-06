from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserListCreateApiView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', views.CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user_retrieve_update_destroy'),
    path('users/<int:pk>/posts/', views.UserPostListAPIView.as_view(), name='user_posts'),
    path('posts/', views.PostListCreateApiView.as_view(), name="post_list_create"),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_retrieve_update_destroy')
]
