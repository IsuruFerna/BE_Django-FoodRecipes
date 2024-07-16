from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_meals, name="all_meals"),
    path("random/", views.random_ten_meals, name="random_ten_meals"),
    path("search/", views.search_by, name="search"),
]

