from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Podcast = models.CharField(null=True, max_length=300)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Published_Date = models.DateTimeField()

    def __str__(self):
        return self.Title

class Resource(models.Model):
    url = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    description = models.TextField()
    resource_type = models.IntegerField(default=0)
    related = models.ForeignKey('Post', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class User_Feedback(models.Model):
    name = models.CharField(max_length=60)
    feedback = models.TextField()
    related_resource = models.ForeignKey('Resource', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
