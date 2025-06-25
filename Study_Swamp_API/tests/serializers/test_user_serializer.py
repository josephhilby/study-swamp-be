import pytest
from django.test import TestCase
from Study_Swamp_API.models import User
from Study_Swamp_API.serializers import UserSerializer

class TestUser(TestCase):
    def setUp(self):
        self.user = User(first_name="name",
                         last_name="lastname",
                         username="username",
                         email="test@user.com",
                         password="123", )
        self.serialized_user = UserSerializer(self.user)

    def test_user_serialize(self):
        data = self.serialized_user.data
        assert isinstance(data, dict)
        assert len(data) == 6
        assert isinstance(data['username'], str)
        assert isinstance(data['email'], str)
        assert isinstance(data['first_name'], str)
        assert isinstance(data['last_name'], str)