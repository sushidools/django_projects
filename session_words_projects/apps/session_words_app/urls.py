from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'add$', views.add, name="add"),
    url(r'clear$', views.clear, name="clear")   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon