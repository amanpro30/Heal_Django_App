from django.conf.urls import url
from django.urls import path
from . import views
from .views import *



app_name='physiotherapist'

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home),
    path('make_profile/',views.make_profile,name='make_profile'),
    path('modify_profile/',views.modify_profile,name='modify_profile'),
    path('show_profile/',views.Show_Profile,name='show_profile'),
    path('home/', home),
    ]
