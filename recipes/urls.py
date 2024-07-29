from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_meals, name="all_meals"),
    path("random/", views.random_meals, name="random_meals"),
    path("search/", views.search_by, name="search"),
    path("meal/", views.add_meal, name="add_meal"),
    path("category/", views.add_category, name="add_category"),
    path("<uuid:meal_id>", views.meal_edit_delete, name="meal_edit_delete"),
    path("category_get/<uuid:category_id>", views.category_view, name="category_view"),
    path("category/<uuid:category_id>", views.edit_delete_category_view, name="category_edit_delete"),
]

