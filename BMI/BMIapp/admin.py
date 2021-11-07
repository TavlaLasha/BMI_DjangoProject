from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, User_Logs

admin.site.register(User, UserAdmin)
admin.site.register(User_Logs)