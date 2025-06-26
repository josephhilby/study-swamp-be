import pytest
from django.test import TestCase
from Study_Swamp_API.models import User

class UserTests(TestCase):
    def setUp(self):
        self.user = User(first_name="name",
                         last_name="lastname",
                         email="test@user.com",
                         password="123",)

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_user_state(self):
        assert self.user.first_name == "name"