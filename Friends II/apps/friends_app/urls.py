from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^friends$', views.friends),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]
