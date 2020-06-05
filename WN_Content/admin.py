from django.contrib import admin
from .models import Post, Feedback, Resource

admin.site.register(Post)
admin.site.register(Resource)
admin.site.register(Feedback)
