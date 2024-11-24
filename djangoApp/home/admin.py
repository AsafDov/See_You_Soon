from django.contrib import admin

# Register your models here.
from .models import User, Friend, Meeting  

admin.site.register(User)
admin.site.register(Friend)  
admin.site.register(Meeting)