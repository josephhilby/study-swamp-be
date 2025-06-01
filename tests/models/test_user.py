import pytest
from django.test import TestCase
from Study_Swamp_API.models import User

class TestUser(TestCase):
    def setUp(self):
        self.user = User(name="test name")

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_user_state(self):
        assert self.user.name == "test name"