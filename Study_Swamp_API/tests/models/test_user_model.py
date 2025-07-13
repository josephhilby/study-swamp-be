from django.test import TestCase
from Study_Swamp_API.models import User
from Study_Swamp_API.tests.factories import UserFactory

class UserModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory(first_name='name')

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_user_state(self):
        assert self.user.first_name == "name"