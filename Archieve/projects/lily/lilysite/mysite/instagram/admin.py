from django.contrib import admin

# Register your models here.

from .models import User, Friend, Post, Profile_Pic

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Post)
admin.site.register(Profile_Pic)
