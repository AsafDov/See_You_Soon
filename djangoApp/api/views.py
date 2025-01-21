from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from home.models import Friend, User, Meeting
import numpy as np
from .serializers import FriendSerializer, MeetingSerializer,UserSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    apiUrls = {
        "listUsers":"/listUsers/",
        "listAllFriends":"/listAllFriends/",
        "listUserFriends":"/<str:username>/",
        "addUser":"/addUser/",
        "updateUser":"/updateUser/",
        "deleteUser":"/deleteUser/'<str:username>/",
        "addMeeting":"/addMeeting/'<str:username>/<str:pk>/",
        "deleteMeeting":"/deleteMeeting/'<str:username>/<str:pk>/<str:pk>/",
        "lastMeetingDate":"/lastMeetingDate/'<str:username>/<str:pk>/",
        "addFriendToUser":"<str:username>/addFriend/",
        "getStatistics":"/getStats/<str:username>/<str:friend>/"
    }
    return Response(apiUrls)


@api_view(['GET'])
def listAllFriends(request):
    friends = Friend.objects.all()
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStatistics(request, username, friend):
    user = User.objects.get(username=username)
    friends = Friend.objects.get(username=user,name=friend)

    meetings = Meeting.objects.filter(username=user, friend=friend) 
    dayElapsedList = []
    for meeting in meetings:
        dayElapsedList.append(meeting.daysElapsed)
    print(dayElapsedList)
    avgDays = str(np.mean(dayElapsedList).astype(int))
    maxDays = str(np.max(dayElapsedList))
    print(dayElapsedList, avgDays, maxDays)   

    return JsonResponse({
                            "avg" : avgDays,
                            "max": maxDays
                        })

@api_view(['GET'])
def listUsers(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
    except:
        return Response("No users in database")
    return Response(serializer.data)

@api_view(['GET'])
def listMeetings(request, username,friend):
    try:
        meetings = Meeting.objects.filter(username=username).filter(friend=friend)
    except:
        return Response("No meetings in database")
    
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def addFriend(request):
    serializer = FriendSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(f"{serializer.data} saved")
    
    return Response(f"{serializer.data} failed to save")

@api_view(['POST'])
def updateUser(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerializer(instance = user, data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(f"User {username} Updated to {request.data['username']}")

@api_view(['DELETE'])
def deleteUser(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        return Response(f"User {username} doesnt exist")
    
    user.delete()
    return Response(f"Deleted User {username}")

@api_view(['POST'])
def addMeeting(request):
    friend = Friend.objects.filter(name=request.data['friend']).filter(username=request.data['username'])
    # friend = Friend.objects.all()
    if friend==None:
        return(Response(f"{request.data['username']} doesnt have a friend names {request.data['friend']}"))
    serializer = MeetingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return(Response(f"{serializer.data} saved"))
    
    return(Response(f"{serializer.data} failed to save"))

@api_view(['GET'])
def listFriendMeetings(request):
    pass

@api_view(['GET'])
def listUserFriends(request, username):
    friends = Friend.objects.filter(username=username)
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)




@api_view(['DELETE'])
def deleteMeeting(request):
    pass


@api_view(['POST'])
def lastMeetingDate(request):
    """Last meeting date per friend"""
    pass



