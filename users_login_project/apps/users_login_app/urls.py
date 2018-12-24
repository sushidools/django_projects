from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^users/(?P<id>[0-9]+)/edit$', views.edit),
    url(r'^users/(?P<id>[0-9]+)$', views.show),
    url(r'^create$', views.create),
    url(r'^users/(?P<id>[0-9]+)/destroy$', views.destroy),
    url(r'^users/update$', views.update) # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon