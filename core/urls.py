# CORE/urls.py

from django.urls import path
from core import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('users/', views.UserList.as_view(), name="user_list"),
    # http://127.0.0.1:8000/user/2/
    # path('user/<int:pk>/', views.userProfileView, name='user_profile'),
    # http://127.0.0.1:8000/testuser1/
    path('user/<username>/', views.userProfileView, name='user_profile'),
]
