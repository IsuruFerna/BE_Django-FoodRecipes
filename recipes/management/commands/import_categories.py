from typing import Any
from django.core.management.base import BaseCommand

import requests
import random

from recipes.models import Category
from users.models import CustomUser

# populate category data to DB
def populate_category_data():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
    if response.status_code == 200:
        print("Success!")
        categories = response.json()

        if categories:
            print(len(categories['categories']))
            for category in categories['categories']:
                
                # select random user
                users = CustomUser.objects.all()
                random_num = random.randint(0, users.count() - 1)
                random_user = users[random_num]

                current_category = Category(
                    user=random_user,
                    strCategory=category['strCategory'],
                    strCategoryTumb=category['strCategoryThumb'],
                    strCategoryDescription=category['strCategoryDescription']
                )

                try:
                    current_category.save()
                    print(f"Added: {category['strCategory']}")

                except Exception as e:
                    print(f"something went wrong at {category}. Error: {str(e)}")


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args: Any, **options):
        populate_category_data()

