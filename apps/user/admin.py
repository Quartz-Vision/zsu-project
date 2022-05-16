# from curses.ascii import US
from django.contrib import admin
from apps.user.models import User

admin.site.register(User)
