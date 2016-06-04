from __future__ import unicode_literals
from django.conf.urls import url

from . import views


app_name = 'meals'
urlpatterns = [
	# ex: /meals/
	url(r'^$', views.index, name='index'),
	# ex: /meals/5/
	url(r'^(?P<meal_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /meals/5/results/
	url(r'^(?P<meal_id>[0-9]+)/results/$', views.results, name='results'),
	# ex: /meals/5/act/
	url(r'^(?P<meal_id>[0-9]+)/act/$', views.action, name='action'),
]