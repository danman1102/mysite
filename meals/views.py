from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Meal
import random

# Create your views here.
def index(request):
	latest_meal_list = Meal.objects.filter(category_text='Main Dish').order_by('?')[:5]
	#Meal.objects.order_by('-create_date')[:5]
	context = {
		'latest_meal_list': latest_meal_list,
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