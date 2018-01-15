from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^register$', views.register), 
    url(r'^login$', views.login), 
    url(r'^logout$', views.logout), 
    url(r'^home$', views.home)
]