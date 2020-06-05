from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('WN_Content/post_list/', views.podcasts, name='podcasts'),
    path('WN_Content/selected_podcast/<int:id>', views.selected_podcast, name='selected_podcast'),
    path('WN_Content/type1', views.type1_resources, name='type1_resources'),
    path('WN_Content/selected_type1/<int:id>', views.selected_type1, name='selected_type1'),
    path('WN_Content/type2', views.type2_resources, name='type2_resources'),
    path('WN_Content/selected_type2/<int:id>', views.selected_type2, name='selected_type2'),
]