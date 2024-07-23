from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from ..models import CustomUser
from ..utils import user_generator

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url=reverse('register')
        self.login_url=reverse('token_obtain_pair')
        self.refresh_token_url=reverse('token_refresh')

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()