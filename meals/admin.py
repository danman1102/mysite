from django.contrib import admin
from .models import Meal,HistoryType,History

# Register your models here.
admin.site.register(Meal)
admin.site.register(HistoryType)
admin.site.register(History)