from django.shortcuts import redirect, render
from .models import  User
from .models import  Friend
from .models import  Meeting
from django.utils.timezone import now  # Import timezone aware `now`
from django.conf import settings
from home.forms import AddFriendForm, MeetingForm, UserForm, FriendForm


# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        if "saveUser" in request.POST:
            form = UserForm(request.POST)
            form.save()
            pass
        elif "editUser" in request.POST:
            pass
        elif "deleteUser" in request.POST:
            username = request.POST.get("deleteUser")
            user = User.objects.get(username = username )
            user.delete()
        
    form = UserForm()
    users = User.objects.all()
    friends = Friend.objects.all()
    meetings = Meeting.objects.all()

    context["form"] = form
    context['users'] = users
    context['friends'] = friends
    context['meetings'] = meetings
    context['title'] = "Home"
    return render(request, "index.html", context=context)

def userPage(request, username):
    context = {}
    print(f"username : {username}")
    user = User.objects.get(username=username)
    friends = Friend.objects.filter(username=user)

    if request.method == "POST":
        if "saveMeeting" in request.POST:
            form = MeetingForm(request.POST,user=user)
            if form.is_valid():
                print("data saved")
                meeting=form.save(commit=False)
                meeting.username=user
                meeting.save()
            else:
                print(form.errors)

        elif "editUser" in request.POST:
            pass
        elif "deleteMeeting" in request.POST:
            meetingId = request.POST.get("deleteMeeting")
            meeting = Meeting.objects.get(id=meetingId)
            friendMeetings = Meeting.objects.filter(username=user,friend=meeting.friend)
            print(friendMeetings)
            if len(friendMeetings)==1:
                meeting.friend.delete()
            else:
                meeting.delete()

    form = MeetingForm(user=user)
    context['meetings'] = Meeting.objects.filter(username=user)
    context['user'] = user
    context['friends'] = friends
    context['title'] = username
    context['lastMeeting'] = []
    context["form"] = form
    # print(context["meetings"])

    for friend in friends:
        context["lastMeeting"].append(Meeting.objects.filter(username=user, friend=friend).order_by("-date").first())
    return render(request, "userPage.html", context=context)

def friendsPage(request, username):
    context = {}
    user = User.objects.get(username=username)
    if request.method == "POST":
        if "saveFriend" in request.POST:
            form = FriendForm(request.POST,user) 
            if form.is_valid:
                print("saving new friend")
                friend=form.save(commit=False)
                friend.username=user
                friend.save()
            else:
                print(form.errors)
            pass
        elif "editUser" in request.POST:
            pass
        elif "deleteFriend" in request.POST:
            friendName = request.POST.get("deleteFriend")
            friendToDelete = Friend.objects.get(username=user,name=friendName)
            friendToDelete.delete()
        
    form = FriendForm()
    user = User.objects.get(username=username)
    friends = Friend.objects.filter(username=user)
    context["user"] = user
    context["friends"] = friends 
    context["form"]= form

    return render(request, "userFriends.html", context=context)

def addFriendPage(request, username):
    context = {}
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = AddFriendForm(request.POST)
        if form.is_valid:
            friendName = request.POST["name"] 
            friend, isNewFriend = Friend.objects.get_or_create(username=user,name=friendName)
            if not isNewFriend:
                print("Friend already exists")
                return render(request, "addFriend.html",context={"exists":True,"form":form, "user":user})
            print("Saving new friend")
            firstMeeting=form.save(commit=False)
            firstMeeting.friend=friend
            firstMeeting.username=user
            # friend.save()
            firstMeeting.save()
        else:
            print(form.errors)

    form = AddFriendForm()
    friends = Friend.objects.filter(username=user)
    context["friends"] = friends 
    context["user"] = user
    context["form"] = form
     
    return render(request, "addFriend.html",context=context)

