from django.conf.urls import url
from . import views           # This line is new!         # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^show(?P<number>\d+)$', views.show),
    url(r'^edit(?P<number>\d+)$', views.edit),
    url(r'^destroy(?P<number>\d+)$', views.destroy)   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon