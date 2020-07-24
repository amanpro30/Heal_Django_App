from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from .views import *

app_name="lab"

urlpatterns = [
    path('lab_home/',lab_home, name='lab_home'),
    path('add_test/',add_test, name='add_test'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
