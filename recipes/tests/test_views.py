from .test_setup import testSetUp
from rest_framework import status
from utils.utils import category_generator, meal_generator, user_generator

from users.models import CustomUser
from ..models import Category, Meal

class TestViews(testSetUp):

    def test_non_register_user_can_not_add_meals(self):
        res = self.client.post(self.add_meal_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

"""

    def test_registerd_users_can_add_meals(self):
        user = user_generator()

        # register new user
        userRes = self.client.post(self.register_user_url, user)
        self.assertEqual(userRes.status_code, status.HTTP_201_CREATED)

        user_id = userRes.data['id']
        print(f"this is uder id: {user_id}")
        
        # login registed user
        loginRes = self.client.post(self.login_url, user)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(loginRes.status_code, status.HTTP_200_OK)

        # create category
        # token = loginRes.data['access']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        # category = request.POST.copy()
        # category['user'] = user_id

        # categoryRes = self.client.post(self.add_category_url, category)
        # self.assertEqual(categoryRes.status_code, status.HTTP_201_CREATED)
        

"""


        