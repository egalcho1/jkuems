from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
class UserAdmin(admin.ModelAdmin):
  list_display =['username', 'password','type']
  admin.site.register(Request)
  
