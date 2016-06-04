from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Meal(models.Model):
	meal_name = models.CharField(max_length=200)
	create_date = models.DateTimeField('Date Added')
	counter = models.IntegerField(default=0)
	category_text = models.CharField(max_length=200)
	def __str__(self):
		return self.meal_name
	def was_added_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days-1) <= self.pub_date <= now
	
@python_2_unicode_compatible
class History(models.Model):
	meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
	history_type = models.CharField(max_length=200)
	event_count = models.IntegerField(default=0)
	time_stamp = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.history_type
		