from django.urls import path
from . import views


urlpatterns = [
    path('WN_Content/home/', views.home, name='home'),
    path('WN_Content/post_list/', views.podcasts, name='podcasts'),
    path('WN_Content/selected_podcast/<int:id>', views.selected_podcast, name='selected_podcast'),
    path('WN_Content/listed_resources/<int:resource_type>', views.listed_resources, name='listed_resources'),
    path('WN_Content/selected_resource/<int:id>/<int:resource_type>', views.selected_resource, name='selected_resource')
]