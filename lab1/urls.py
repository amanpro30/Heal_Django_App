from django.conf.urls import url
from django.urls import path
from . import views
from .views import *



app_name='lab1'

urlpatterns = [
    path('',views.index,name='index'),
    # path('slot/', views.home),
    path('make_profile/',views.make_profile,name='lab_make_profile'),
    path('modify_profile/',views.modify_profile,name='lab_modify_profile'),
    path('show_profile/',views.Show_Profile,name='lab_show_profile'),
    path('show_tests/',views.tests, name='lab_show_tests'),
    path('lab_bookings/',views.show_bookings, name='lab_show_bookings'),
    path('assign_collector/',views.assign_collector, name='lab_assign_collector'),
    path('home/', lab_home, name='lab_home'),
    path('date_add/',views.DateCreate.as_view(),name='lab_date_create'),
    url(r'^date_add/(?P<pk>[0-9]+)/slot/$', views.create_slot, name='lab_create_slot'),
    path('slots/',views.show_slots,name='show_slots'),
    path('complaint_feedback/', views.ComplaintFeedbackCreate.as_view(template_name="lab1/new_file.html"), name='lab_complaint_feedback'),
    path('show_complaint_feedback/', views.show_complaint_feedback, name='lab_show_complaint_feedback'),
    url(r'^delete_slot/(?P<slot_id>[0-9]+)$',views.delete_slot,name='lab_delete_slot'),
    url(r'^select_collector/(?P<pk>[0-9]+)$',views.select_collector,name='select_collector'),
    url(r'^assign_collector_to_test/(?P<collector_id>[0-9]+)$',views.assign_collector_to_test,name='assign_collector_to_test'),
    ]
