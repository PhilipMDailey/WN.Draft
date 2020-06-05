from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Resource
from django.utils import timezone


def home(request):
    return HttpResponse('Home Page')

def podcasts(request):
    posts = Post.objects.filter(Published_Date__lte=timezone.now()).order_by('Published_Date')
    return render(request, 'WN_Content/post_list.html', {'posts': posts})

def selected_podcast(request, id):
    post = Post.objects.get(id=id)
    posts = Post.objects.filter(Published_Date__lte=timezone.now()).order_by('Published_Date').exclude(id=id)
    resource = Resource.objects.get(id=id)
    related1 = Resource.objects.filter(type1=True).order_by('title')
    related2 = Resource.objects.filter(type2=True).order_by('title')
    context = {
        'posts':posts,
        'post':post,
        'related1':related1,
        'resource':resource,
        'related2':related2
    }
    return render(request, 'WN_Content/selected_podcast.html', context)

def type1_resources(request):
    posts = Resource.objects.filter(type1 = True).order_by('title')
    return render(request, 'WN_Content/type1.html', {'posts':posts})

def selected_type1(request, id):
    post = Resource.objects.get(id=id)
    posts = Resource.objects.filter(type1 = True).order_by('title').exclude(id=id)
    context = {
        'posts':posts,
        'post':post
    }
    return render(request, 'WN_Content/selected_type1.html', context)

def type2_resources(request):
    posts = Resource.objects.filter(type2 = True).order_by('title')
    return render(request, 'WN_Content/type2.html', {'posts':posts})  

def selected_type2(request, id):
    post = Resource.objects.get(id=id)
    posts = Resource.objects.filter(type2 = True).order_by('title').exclude(id=id)
    context = {
        'posts':posts,
        'post':post
    }
    return render(request, 'WN_Content/selected_type2.html', context)

"""h
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'podcasts/post_list.html', {'post': posts})
"""