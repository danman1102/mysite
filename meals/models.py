from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from categories.base import CategoryBase
from taggit.managers import TaggableManager

# Create your models here.


@python_2_unicode_compatible
class Meal(models.Model):
	meal_name = models.CharField(max_length=255)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	last_suggested_date = models.DateTimeField(null=True, blank=True)
	last_selected_date = models.DateTimeField(null=True, blank=True)
	counter = models.IntegerField(default=0)
	category_text = models.CharField(max_length=200)
	tags = TaggableManager()
	def __str__(self):
		return self.meal_name
	def was_added_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days-1) <= self.pub_date <= now
	def suggested_count(self):
		return self.history_set.filter(history_type='Suggested').count()
	
@python_2_unicode_compatible
class HistoryType(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	
	class Meta:
		verbose_name = 'history-type'
		verbose_name_plural = 'history-types'
	def __unicode__(self):
		return u'%s' % self.title
	def __str__(self):
		return self.title
	
@python_2_unicode_compatible
class History(models.Model):
	Suggested = 'Suggested'
	Selected = 'Selected'
	history_type_choices = (
		(Suggested, 'Suggested'),
		(Selected, 'Selected'))
	meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
	history_type = models.CharField(max_length=50,choices=history_type_choices,default=Suggested)
	event_count = models.IntegerField(default=0)
	time_stamp = models.DateTimeField(default=timezone.now)
	def __unicode__(self):
		return u'%s' % str(self.history_type)
	def __str__(self):
		return '%s %s at %s' %(self.history_type,self.meal,self.time_stamp)
		
