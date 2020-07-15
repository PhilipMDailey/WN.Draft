from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Resource
from .models import User_Feedback
from django.utils import timezone
from django.urls import resolve
from .forms import UserFeedback
from django.views.generic import CreateView


def home(request):
    latest_podcast = Post.objects.filter(Published_Date__lte=timezone.now()).order_by('Published_Date').first()
    return render(request, 'WN_Content/home.html', {'latest_podcast':latest_podcast})

def podcasts(request):
    posts = Post.objects.filter(Published_Date__lte=timezone.now()).order_by('Published_Date')
    return render(request, 'WN_Content/post_list.html', {'posts': posts})

def selected_podcast(request, id):
    post = Post.objects.get(id=id)
    posts = Post.objects.filter(Published_Date__lte=timezone.now()).order_by('Published_Date').exclude(id=id)
    relatedpost1 = Resource.objects.filter(related = post, resource_type = 1).order_by('title')
    relatedpost2 = Resource.objects.filter(related = post, resource_type = 2).order_by('title')
    relatedpost3 = Resource.objects.filter(related = post, resource_type = 3).order_by('title')
    context = {
        'posts':posts,
        'post':post,
        'relatedpost1':relatedpost1,
        'relatedpost2':relatedpost2,
        'relatedpost3':relatedpost3
    }
    return render(request, 'WN_Content/selected_podcast.html', context)

def listed_resources(request, resource_type):
    link = Resource.objects.filter(resource_type=resource_type)
    type1 = Resource.objects.filter(resource_type = 1).order_by('title')
    type2 = Resource.objects.filter(resource_type = 2).order_by('title')
    type3 = Resource.objects.filter(resource_type = 3).order_by('title')
    context = {
        'type1':type1,
        'type2':type2,
        'type3':type3,
        'link':link
    }
    return render(request, 'WN_Content/listed_resources.html', context)

def selected_resource(request, id, resource_type):
    resource = Resource.objects.get(id=id)
    type_check = Resource.objects.filter(resource_type=resource_type).order_by('title').exclude(id=id)
    url_name = resolve(request.path).url_name
    listed_feedback = User_Feedback.objects.order_by('-id').filter(related_resource=resource)
    feedback_form = UserFeedback(request.POST or None)
    if feedback_form.is_valid():
            model = feedback_form.save()
            model.related_resource = resource 
            model.save()
            feedback_form = UserFeedback()
    context = {
        'type_check':type_check,
        'resource':resource,
        'url_name':url_name,
        'feedback_form':feedback_form,
        'listed_feedback':listed_feedback
    }
    return render(request, 'WN_Content/selected_resource.html', context)
    


# def type2_resources(request):
#     posts = Resource.objects.filter(type2 = True).order_by('title')
#     return render(request, 'WN_Content/type2.html', {'posts':posts})  

# def selected_type2(request, id):
#     resource = Resource.objects.get(id=id)
#     resources = Resource.objects.filter(type2 = True).order_by('title').exclude(id=id)
#     context = {
#         'resources':resources,
#         'resource':resource
#     }
#     return render(request, 'WN_Content/selected_type2.html', context)

"""h
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'podcasts/post_list.html', {'post': posts})
"""