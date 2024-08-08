from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_meals, name="all_meals"),
    path("random/", views.random_meals, name="random_meals"),
    path("search/", views.search_by, name="search"),
    path("meal/", views.add_meal, name="add_meal"),
  
    path("<uuid:meal_id>", views.meal_edit_delete, name="meal_edit_delete"),

    ###### categories:
    # add category
    path("category/", views.add_category, name="add_category"), 

    # get all categories
    path("categories/", views.all_categories, name="categories_all"),

    # get, patch, delete category
    path("category/<uuid:category_id>", views.category_view, name="category_view"),
    
]

