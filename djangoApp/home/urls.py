"""
URL configuration for FriendTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.userPage, name="home"), # delete when you want to create login page
    path('<str:username>/', views.userPage, name="userHome"),
    path('<str:username>/friends/', views.friendsPage, name="userFriends"),
    path('<str:username>/addFriend/', views.addFriendPage, name="addFriend")
]
