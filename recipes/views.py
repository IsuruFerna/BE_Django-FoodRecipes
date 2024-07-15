from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.paginator import Paginator

import random

from recipes.models import Meal

# gets all the meals with paginator
# /recipes/?page_num=1&per_page=10
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

# gets random 10 meals
# /recipes/random/
def random_ten_meals(request):
    meals = Meal.objects.all()
    meals_amount = meals.count()
    random_nums = []
    random_meals = []
    
    # controls util it generates 10 unique random numbers
    while len(random_nums) < 10:
        generated_num = random.randrange(meals_amount)
        if not generated_num in random_nums:
            random_nums.append(generated_num)

            # fills random meal corresponds the generated random number
            random_meals.append(meals[generated_num])

    return JsonResponse(serialize('json', random_meals), safe=False)


