from .test_setup import TestSetUp
from ..models import CustomUser

from utils.utils import user_generator


class TestViews(TestSetUp):

    def test_user_cannot_register(self):
        res = self.client.post(self.register_url)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)

    def test_user_can_register(self):
        user = user_generator()
        
        res = self.client.post(self.register_url, user)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 201)


    def test_username_must_be_unique(self):
        user = user_generator()

        # register an user
        res = self.client.post(self.register_url, user)
        self.assertEqual(res.status_code, 201)

        # use the username of previously registed user
        duplicate_username_user = user_generator()
        duplicate_username_user['username'] = user['username']
        res = self.client.post(self.register_url, duplicate_username_user)

        self.assertEqual(res.status_code, 400)


    def test_email_must_be_unique(self):
        user = user_generator()

        # register an user
        res = self.client.post(self.register_url, user)
        self.assertEqual(res.status_code, 201)

        # use the email of previously registed user
        duplicate_email_user = user_generator()
        duplicate_email_user['email'] = user['email']
        res = self.client.post(self.register_url, duplicate_email_user)

        self.assertEqual(res.status_code, 400)

