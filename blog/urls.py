from django.urls import path, include
from .import views 
from django.conf.urls import url



urlpatterns = [
    path('add/', views.add_blog, name='add_blog'),
    path('b/', views.show, name="show"),
    path('b/<slug:slug>/', views.view_post, name='post_detail'),
    path('nurse/', views.nurse, name='nurse'),
    # path('doctor/?P<spec>', views.doctor, name='doctor'),
    path('nurse/<id>/', views.nurse_detail, name='nurse-detail'),
    path('nurse/<id>/reply/', views.nurse_reply, name='nurse-reply'),
    
]