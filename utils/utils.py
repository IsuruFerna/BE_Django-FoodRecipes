from faker import Faker
from faker_food import FoodProvider
from rest_framework.pagination import PageNumberPagination

# paginator response for meal views
def paginator_response(data, request, Serializer):
    
    # sets pagination using django_rest and it's global settings from the settings.py file under REST_FRAMEWORK list
    paginator = PageNumberPagination()
    paginated_data = paginator.paginate_queryset(data, request)
    serialized_data = Serializer(paginated_data, many=True)

    return paginator.get_paginated_response(serialized_data.data)

# generates users for unit test
def user_generator():
    faker = Faker()
    return {
        'email': faker.email(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'username': faker.user_name(),
        'password': faker.password()
    }

def category_generator():
    fake = Faker()
    fake.add_provider(FoodProvider)

    return {
        "user": "",
        "strCategory":fake.ethnic_category(),
        "strCategoryTumb":fake.url(),
        "strCategoryDescription":fake.dish_description()                              
    }

def meal_generator(user, category):
    fake = Faker()
    fake.add_provider(FoodProvider)

    return {
        "user": user,
        "strMeal": fake.dish(),
        "strDrinkAlternate": "",
        "strCategory": category,
        "strArea": fake.country(),
        "strInstructions": fake.dish_description(),
        "strMealThumb": fake.url(),
        "strTags": "Meat,Stew",
        "strYoutube": fake.url(),
        "strIngredient1": fake.ingredient(),
        "strIngredient2": fake.ingredient(), 
        "strIngredient3": "", 
        "strIngredient4": "", 
        "strMeasure1": fake.metric_measurement(),
        "strMeasure2": fake.measurement_size(),
        "strSource": fake.url(),
    }


