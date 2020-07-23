from django.urls import path, include
from .import views 
from django.conf.urls import url



urlpatterns = [
    path('add/', views.add_blog, name='add_blog'),
    path('b/', views.show, name="show"),
    path('b/<slug:slug>/', views.view_post, name='post_detail'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor/?P<spec>', views.doctor, name='doctor'),
    path('doctor/<id>/', views.doctor_detail, name='doctor-detail'),
    path('doctor/<id>/reply/', views.doctor_reply, name='doctor-reply'),
    
]