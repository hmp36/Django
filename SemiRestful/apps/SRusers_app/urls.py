from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^add_user$', views.add_user),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^update_user/(?P<user_id>\d+)$', views.update),
    url(r'^delete/(?P<user_id>\d+)$', views.remove),
]
