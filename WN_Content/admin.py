from django.contrib import admin
from .models import Post, User_Feedback, Resource

admin.site.register(Post)
admin.site.register(Resource)
admin.site.register(User_Feedback)