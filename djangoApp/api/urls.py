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
import datetime
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('apiOverview/', views.apiOverview, name="apiOverview"),
    path('listUsers/', views.listUsers, name="listUsers"),
    path('listAllFriends/', views.listAllFriends, name="listFriends"),
    path('addUser/', views.addUser, name="addUser"),
    path('updateUser/<str:username>/', views.updateUser, name="updateUser"),
    path('deleteUser/<str:username>/', views.deleteUser, name="deleteUser"),
    path('addMeeting/', views.addMeeting, name="addMeeting"),
    path('addFriend/', views.addFriend, name="addFriend"),
    path('listFriends/<str:username>/', views.listUserFriends, name="listFriends"),
    path('listMeetings/<str:username>/<str:friend>', views.listMeetings, name="listMeetings"),
    path('getStats/<str:username>/<str:friend>/', views.getStatistics, name="friendStatistics"),
]

addFriend = {
    "username":"asafdov",
    "name":"Shirel"
}
# addUser = {
#     "username":"asafdov",
# }
meeting ={
    "username":"asafish",
    "friend":"shirel",
    "date":datetime.datetime.now(),
    "details":"blah"
}