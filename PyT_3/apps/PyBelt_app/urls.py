from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
    url(r'^remove_wish/(?P<id>\d+)$', views.remove_wish),
   	url(r'^users/(?P<id>\d+)$', views.show_user),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^addItem$', views.addItem),
    url(r'^submitItem$', views.submitItem),
    url(r'^item/(?P<id>\d+)$', views.item),
    url(r'^addWish/(?P<id>\d+)$', views.addWish),
]



# dashboard/(?P<name>\w+)


# /(?P < id >\d +)$
