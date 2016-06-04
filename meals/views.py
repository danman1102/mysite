from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone

from .models import Meal,History,HistoryType
import random

# Create your views here.
def index(request):
	def createHx(meal,type):
		m = Meal.objects.get(meal_name=meal)
		m.history_set.create(history_type=type)
		if type == 'Suggested':
			Meal.objects.filter(meal_name=meal).update(last_suggested_date=timezone.now())
		elif type == 'Selected':
			Meal.objects.filter(meal_name=meal).update(last_selected_date=timezone.now())
		else:
			pass
	#Random 3 Chicken 
	chicken_meal_list = Meal.objects.filter(tags__name__in=["Chicken"]).order_by('?')[:3]
	for c in chicken_meal_list:
		createHx(c,'Suggested')
	
	#Random 3 Beef
	beef_meal_list = Meal.objects.filter(tags__name__in=["Beef"]).order_by('?')[:3]
	for b in beef_meal_list:
		createHx(b,'Suggested')
	
	#Random 1 anything
	other_meal_list = Meal.objects.order_by('?')[:1]
	for o in other_meal_list:
		createHx(o,'Suggested')
	#Meal.objects.order_by('-create_date')[:5]
	context = {
		'chicken_meal_list': chicken_meal_list,
		'beef_meal_list': beef_meal_list,
		'other_meal_list': other_meal_list,
	}
	
	
	return render(request, 'meals/index.html', context)
	
def detail(request, meal_id):
	meal = get_object_or_404(Meal, pk=meal_id)
	return render(request, 'meals/detail.html', {'meal': meal})
	
def results(request, meal_id):
	response = "You're looking at the results of %s" 
	return HttpResponse(response % meal_id)
	
def action(request, meal_id):
	return HttpResponse("You're deciding on %s" %meal_id)