from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.all_meals, name="all_meals")
]

