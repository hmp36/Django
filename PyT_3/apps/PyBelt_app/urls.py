from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success/(?P<first_name>\w+)$', views.success),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login)
]
