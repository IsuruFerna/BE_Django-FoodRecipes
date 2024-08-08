from django.urls import path
from . import views

urlpatterns = [
    # get all the meals
    path("", views.all_meals, name="all_meals"),

    # get random 12 meals
    path("random/", views.random_meals, name="random_meals"),

    # get meals by searching via params: ?name=meal_name&category=meal_category
    path("search/", views.search_by, name="search"),

    # post: add new meal
    path("meal/", views.add_meal, name="add_meal"),

    # get, patch, delete meal
    path("meal/<uuid:meal_id>", views.meal_view, name="meal_view"),

    ###### categories:
    # patch: add category
    path("category/", views.add_category, name="add_category"), 

    # get all categories
    path("categories/", views.all_categories, name="categories_all"),

    # get, patch, delete category
    path("category/<uuid:category_id>", views.category_view, name="category_view"),
    
]

