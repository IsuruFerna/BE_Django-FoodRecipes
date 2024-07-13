from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from recipes.models import Meal

# Create your views here.
def all_meals(request):
    meals = Meal.objects.all()
    return JsonResponse(serialize("json", meals), safe=False)