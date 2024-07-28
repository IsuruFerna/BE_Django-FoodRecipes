from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url=reverse('users:register')
        self.login_url=reverse('users:token_obtain_pair')
        self.refresh_token_url=reverse('users:token_refresh')

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()