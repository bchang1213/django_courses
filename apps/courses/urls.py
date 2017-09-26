from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^add$', views.add),
	url(r'^(?P<course_id>\d+)/remove$', views.remove),
	url(r'^(?P<course_id>\d+)/remove/delete$', views.delete),
  ]