from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^$', views.index),
    url(r'^surveys/process', views.process),
    url(r'^surveys/result', views.result),
    url(r'^reset', views.reset)
]
