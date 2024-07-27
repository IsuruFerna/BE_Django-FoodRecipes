from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_meals, name="all_meals"),
    path("search/", views.search_by, name="search"),
    path("add/", views.add_meal, name="add_meal"),
    path("<uuid:meal_id>", views.meal_edit_delete, name="meal_edit_delete"),
]

