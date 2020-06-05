from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    Video_Url = models.CharField(max_length=100)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Published_Date = models.DateTimeField()

    def __str__(self):
        return self.Title

class Feedback(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Feedback = models.TextField()
    Date = models.DateTimeField()

class Resource(models.Model):
    url = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type1 = models.BooleanField(default=False)
    type2 = models.BooleanField(default=False)
    type3 = models.BooleanField(default=False)
    related = models.ForeignKey('Post', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title