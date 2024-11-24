from django.db import models
from django.utils.timezone import now  # Import timezone aware `now`

class User(models.Model):
    username = models.CharField(max_length=100, unique=True,primary_key=True,default="Asaf")
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Friend(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, primary_key=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    

class Meeting(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    date = models.DateField()  # Field to store the meeting date
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.username.username} met {self.friend.name} on {self.date}'
    
    @property
    def daysElapsed(self):
        """Calculate the days elapsed since the `created` date."""
        return (now().date() - self.date).days

Meeting.objects.order_by("date")