from typing import Any
from django.core.management.base import BaseCommand

import requests
import json

from django.forms import ModelForm
from recipes.models import Category, Meal

class MealForm(ModelForm):
     class Meta:
          model = Meal
          fields = "__all__"

# populate meal data to DB by first letter
def populate_meal_data(firstLetter):

    # gets API data
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={firstLetter}")
    if response.status_code == 200:
        meals = response.json()

        # handles if there are or not meals to the corresponding letter
        if meals and meals['meals'] is not None:

            for meal in meals['meals']:
                
                # selects category of the meal    
                current_category = Category.objects.get(strCategory=meal['strCategory'])

                # make a copy of the meal and removes the strCategory to avoid multiple values
                meal_copy = meal.copy()
                meal_copy.pop("strCategory", None)

                if meal:

                    # destructs and fills the form
                    current_meal = MealForm({
                        **meal_copy,
                        "strCategory":current_category,
                    })

                    # checks form validity and saves
                    if not current_meal.is_valid():
                        print(dict(current_meal.errors))
                        print("modal cant be saved!")
                    else:
                        print("modal saved")
                        current_meal.save()
 
        else:
            print(f"No meals found beginning with the letter '{firstLetter}'")

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args: Any, **options):

        # loops through a to z
        for letter in range(ord('a'), ord('z')):
            populate_meal_data(chr(letter))

