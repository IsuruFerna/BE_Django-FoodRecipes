from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

import random

from users.models import CustomUser
from recipes.models import Category, Meal
from .serializers import MealSerializer

# gets all the meals with paginator
# /recipes/?page_num=1&per_page=10
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def all_meals(request):
    meals = Meal.objects.all().order_by('strMeal')

    # sets pagination using django_rest and it's global settings from the settings.py file under REST_FRAMEWORK list
    paginator = PageNumberPagination()
    paginated_meals = paginator.paginate_queryset(meals, request)
    serialized_meals = MealSerializer(paginated_meals, many=True)

    return paginator.get_paginated_response(serialized_meals.data)


# gets random 10 meals
# /recipes/random/
@api_view(['GET'])
def random_meals(request):
    meals = Meal.objects.all()
    meals_amount = meals.count()
    random_nums = []
    random_meals = []
    
    # controls util it generates 12 unique random numbers
    while len(random_nums) < 12:
        generated_num = random.randrange(meals_amount)
        if not generated_num in random_nums:
            random_nums.append(generated_num)

            # fills random meal corresponds the generated random number
            random_meals.append(meals[generated_num])

    return JsonResponse(serialize('json', random_meals), safe=False)

# search meals by name and category
# /recipers/search/?name=meal_name&category=meal_category
def search_by(request):
    
    # required_parm_fields = ("name", "category")
    # for more improvements with large number of params
    # https://forum.djangoproject.com/t/parsing-and-validating-query-params-from-get-request/24308

    meal_name = request.GET.get('name')
    meal_category = request.GET.get('category')

    # returns param response as paginated json
    def serialized_paginator_response(data):
        page_number = int(request.GET.get('page_num', 1))
        items_per_page = int(request.GET.get('per_page', 12))

        paginator = Paginator(data, items_per_page)
        page_obj = paginator.get_page(page_number)

        serialized_data = serialize('json', page_obj)
    
        return JsonResponse({
            'data': serialized_data,
            'meta': {
                'page': page_obj.number,
                'per_page': items_per_page,
                'total_pages': paginator.num_pages,
                'total_items': paginator.count
            }
        })
    
    if meal_name and meal_category:
        # filters and gets as a list of categorise according to name similarities
        categories = Category.objects.filter(strCategory__contains=meal_category)

        # joins multiples querysets into a unique list by provided category name
        meals = []
        if categories:
            for category in categories:
                meals.extend(Meal.objects.filter(Q(strCategory__strCategory__contains=meal_category) & 
                                                 Q(strMeal__contains=meal_name)))

            return serialized_paginator_response(meals)

        # when no meal found with the provided name and category
        if not meals:
            return JsonResponse({"message": f"No meal found for corresponding name: '{meal_name}' and category: '{meal_category}'"}, status=404)
        
        return serialized_paginator_response(meals)       
    
    if meal_name:
        meals = Meal.objects.filter(strMeal__contains=meal_name).order_by('strMeal')

        # when thre are no meals to provided name
        if not meals:
            print("running inside statement")
            return JsonResponse({"message": f"No meal found for: {meal_name}"}, status=404)
        
        return serialized_paginator_response(meals)
        

    if meal_category:
        # filters and gets as a list of categorise according to name similarities
        categories = Category.objects.filter(strCategory__contains=meal_category)

        # joins multiples querysets into a unique list by provided category name
        meals = []
        if categories:
            for category in categories:
                meals.extend(Meal.objects.filter(strCategory=category))

            return serialized_paginator_response(meals)
        
        # when thre are no categories for provide category
        return JsonResponse({"message": f"No category found for: {meal_category}"}, status=404)
    
    # returns when request doesn't match with any required params
    return JsonResponse({"error": "Missing query params"}, 
            status=404
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_meal(request):
    # if request.method == 'POST':
    user = CustomUser.objects.get(id=request.user.id)
    category = Category()

    meal_serializer = MealSerializer(request.data)

    if meal_serializer.is_valid: 
        print(meal_serializer.validated_data)
    
    
        
    print(f"this is the user {user}")


    return Response(status=status.HTTP_200_OK)

