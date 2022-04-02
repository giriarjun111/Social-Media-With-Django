from django.contrib import admin
from .models import Post, Comment, userProfile, Notification, ThreadModel

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(userProfile)
admin.site.register(Notification)
admin.site.register(ThreadModel)