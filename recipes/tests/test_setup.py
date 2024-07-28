from django.urls import reverse
from rest_framework.test import APITestCase

from utils.utils import category_generator, meal_generator, user_generator
from users.models import CustomUser
from ..models import Category, Meal

class testSetUp(APITestCase):
    def setUp(self) -> None:
        # urls
        self.add_meal_url = reverse('add_meal')
        self.add_category_url = reverse('add_category')
        
        self.register_user_url = reverse('users:register')
        self.login_url=reverse('users:token_obtain_pair')
        self.refresh_token_url=reverse('users:token_refresh')

        # setting instences
        user = CustomUser.objects.create(**user_generator())
        # category = Category.objects.create(**category_generator(user=user))
        # meal = Meal.objects.create(**meal_generator(user=user, category=category))

        self.user = user
        # self.category = category
        # self.meal = meal

        
        


        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()