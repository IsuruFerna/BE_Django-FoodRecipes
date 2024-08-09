from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from drf_spectacular.utils import extend_schema

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

import random

from users.models import CustomUser
from recipes.models import Category, Meal
from .serializers import CategorySerializer, MealSerializer
from utils.utils import paginator_response


# gets all the meals with paginator
# /recipes/?page_num=1&per_page=10
@extend_schema(responses=MealSerializer)
@api_view(['GET'])
def all_meals(request):
    meals = Meal.objects.all().order_by('strMeal')

    return paginator_response(meals, request, MealSerializer)



# gets random 12 meals
# /recipes/random/
@extend_schema(responses=MealSerializer)
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
    
    serialized_meals = MealSerializer(random_meals, many=True)
    
    return Response(
        serialized_meals.data,
        status=status.HTTP_200_OK
    )



# search meals by name and category
# /recipes/search/?name=meal_name&category=meal_category
@extend_schema(responses=MealSerializer)
@api_view(['GET'])
def search_by(request):
    
    # required_parm_fields = ("name", "category")
    # for more improvements with large number of params
    # https://forum.djangoproject.com/t/parsing-and-validating-query-params-from-get-request/24308

    meal_name = request.GET.get('name')
    meal_category = request.GET.get('category')

    # converts all the first letters to uppercase
    if meal_name:
        meal_name = meal_name.title()

    if meal_category:
        meal_category = meal_category.title()

    if meal_name and meal_category:
        # filters and gets as a list of categorise according to name similarities
        categories = Category.objects.filter(strCategory__contains=meal_category)

        # joins multiples querysets into a unique list by provided category name
        meals = []
        if categories:
            for category in categories:
                meals.extend(Meal.objects.filter(Q(strCategory__strCategory__contains=meal_category) & 
                                                 Q(strMeal__contains=meal_name)))
                
            return paginator_response(meals, request, MealSerializer)

        # when no meal found with the provided name and category
        if not meals:
            return JsonResponse({"message": f"No meal found for corresponding name: '{meal_name}' and category: '{meal_category}'"}, status=status.HTTP_404_NOT_FOUND)
          
        return paginator_response(meals, request, MealSerializer)    
    
    if meal_name:
        meals = Meal.objects.filter(strMeal__contains=meal_name).order_by('strMeal')

        # when thre are no meals to provided name
        if not meals:
            print("running inside statement")
            return JsonResponse({"message": f"No meal found for: {meal_name}"}, status=404)

        return paginator_response(meals, request, MealSerializer)
        

    if meal_category:
        # filters and gets as a list of categorise according to name similarities
        categories = Category.objects.filter(strCategory__contains=meal_category)

        # joins multiples querysets into a unique list by provided category name
        meals = []
        if categories:
            for category in categories:
                meals.extend(Meal.objects.filter(strCategory=category))

            return paginator_response(meals, request, MealSerializer)
        
        # when thre are no categories for provide category
        return Response({"message": f"No category found for: {meal_category}"}, status=status.HTTP_404_NOT_FOUND)
    
    # returns when request doesn't match with any required params
    return Response({"error": "Missing query params"}, 
            status=status.HTTP_404_NOT_FOUND
        )



# add new meal 
# /recipes/meal/
@extend_schema(
    request=MealSerializer,
    responses=MealSerializer
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_meal(request):

    # get data
    data = request.data
    user = CustomUser.objects.get(id=request.user.id)

    # sets category
    incomming_category = data['strCategory']
    meal_category = Category.objects.filter(strCategory=incomming_category.title()).first()

    if not meal_category:
        return Response(
            {"error": f"Category '{incomming_category} does not exist."},
            status=status.HTTP_404_NOT_FOUND         
        )

    # check data validity before saving
    meal_serializer = MealSerializer(data=data)
    if not meal_serializer.is_valid(): 
        return Response(meal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # save data
    meal_serializer.save(user=user, strCategory=meal_category)

    return Response(meal_serializer.data, status=status.HTTP_200_OK)


# get, edit or delete meal
# /recipes/meal/<uuid:id>
@extend_schema(
    request=MealSerializer,
    responses=MealSerializer
)
@api_view(['GET', 'DELETE', 'PATCH'])
def meal_view(request, meal_id):

    # check if the given meal is already exsists in the db
    try:
        meal = Meal.objects.get(pk=meal_id)

    except ObjectDoesNotExist:
        return Response(
            {"error": f"Meal does not found with Id: {meal_id}"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # get request
    if request.method == 'GET':
        serialized_meal = MealSerializer(meal)
        return Response(
            serialized_meal.data,
            status=status.HTTP_200_OK
        )
    
    # patch and delete request
    if request.user.is_authenticated:

        meal_user = meal.user
        logged_user = request.user

        # check weather the user has access to modify his own listed data
        if meal_user.id != logged_user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # patch request
        if request.method == 'PATCH':
            data = request.data

            # category = None
            custom_errors = {}

            # check if request data provided a category
            meal_category = data['strCategory']

            if meal_category:
                category = Category.objects.filter(strCategory=meal_category.title()).first()

                if not category:
                    custom_errors['Category error'] = "Provided category doesn't found. Please create a new category before adding it!"

                    return Response(custom_errors, status=status.HTTP_404_NOT_FOUND)

            meal_serializer = MealSerializer(instance=meal, data=data, partial=True)
            
            # validate data
            if not meal_serializer.is_valid():

                # update custom errors because if there is already an error in category, I don't want to loose it from the 'custom_errors' dictionary
                custom_errors.update(meal_serializer.errors)
                return Response(custom_errors, status=status.HTTP_400_BAD_REQUEST)
            
            # update meal
            if category:
                meal_serializer.save(strCategory=category)
            else:
                meal_serializer.save()

            return Response(
                meal_serializer.data,
                status=status.HTTP_200_OK
            )

        if request.method == 'DELETE':
            # delete meal
            meal.delete()

            return Response({
                "message": "Meal successfully deleted!"
            }, status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_401_UNAUTHORIZED)



################################## CATEGORIES #################################################


# add new category
# /recipes/category/
@extend_schema(
    request=CategorySerializer,
    responses=CategorySerializer
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_category(request):
    
    category = request.data.copy()
    category['user'] = request.user.id

    serialized_category = CategorySerializer(data=category)

    if not serialized_category.is_valid():
        return Response(serialized_category.errors, status=status.HTTP_400_BAD_REQUEST)

    serialized_category.save()

    return Response(serialized_category.data, status=status.HTTP_201_CREATED)



# get all the categories
# recipes/categories/
@extend_schema(responses=CategorySerializer)
@api_view(['GET'])
def all_categories(request):

    categories = Category.objects.all().order_by('strCategory')
    return paginator_response(categories, request, CategorySerializer)



# get, modify or delete specific category
# recipes/categoriy/<uuid:category_id>
@extend_schema(
    request=CategorySerializer,
    responses=CategorySerializer
)
@api_view(['GET', 'PATCH', 'DELETE'])
def category_view(request, category_id):

    # check if the given category is already exsists in the db
    try:
        category = Category.objects.get(pk=category_id)

    except ObjectDoesNotExist:
        return Response(
            {"error": f"Category does not found with Id: {category_id}"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # get requests
    if request.method == 'GET':

        serialized_category = CategorySerializer(category)
        return Response(
            serialized_category.data,
            status=status.HTTP_200_OK
        )
    
    # edit or delete requests
    if request.user.is_authenticated:
        
        # retriave data for modification
        data = request.data

        # check if the category is created by the requsting user
        if category.user.id != request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        # updates modifications
        if request.method == 'PATCH':
            serialized_category = CategorySerializer(instance=category, data=data)

            # validate data
            if not serialized_category.is_valid(): 
                return Response(
                    serialized_category.errors, status=status.HTTP_400_BAD_REQUEST
                )
            
            serialized_category.save()
            return Response(
                serialized_category.data, status=status.HTTP_200_OK
            )    

        # delete category
        if request.method == 'DELETE':
            category.delete()

            return Response(
                {"message": f"Category ID: {category_id} successfully deleted!"},
                status=status.HTTP_404_NOT_FOUND
            )

    return Response(status=status.HTTP_401_UNAUTHORIZED)
    






