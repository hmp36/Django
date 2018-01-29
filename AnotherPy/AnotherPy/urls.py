from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    
    url(r'^', include('apps.SuperApp.urls')),
    url(r'^', include("apps.Friends.urls"))
]
