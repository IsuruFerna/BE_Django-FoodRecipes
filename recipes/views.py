from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.paginator import Paginator

from recipes.models import Meal

# gets all the meals with paginator
def all_meals(request):
    meals = Meal.objects.all()

    page_number = int(request.GET.get('page_num', 1))
    items_per_page = int(request.GET.get('per_page', 10))

    paginator = Paginator(meals, items_per_page)
    page_obj = paginator.get_page(page_number)

    serialized_meals = serialize('json', page_obj)

    return JsonResponse({
        'data': serialized_meals,
        'meta': {
            'page': page_obj.number,
            'per_page': items_per_page,
            'total_pages': paginator.num_pages,
            'total_items': paginator.count
        }
    })