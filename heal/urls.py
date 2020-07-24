from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from accounts.views import index
from .views import home_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    # path('home/', home),
    # path('', index),
    path('lab/',include('lab.urls')),
    path('nurse/', include('nurse.urls')),
    path('patient/', include('patient.urls')),
    path('report/', include('report.urls')),
    url('',include('adminpage.urls')),
    path('', home_page),
    path('physiotherapist/',include('physiotherapist.urls')),
    path('lab1/',include('lab1.urls')),
    path('samplecollector/',include('samplecollector.urls')),


] 
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
