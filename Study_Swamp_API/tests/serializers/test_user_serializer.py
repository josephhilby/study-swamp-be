import pytest
from django.test import TestCase
from Study_Swamp_API.models import User
from Study_Swamp_API.serializers import UserSerializer

class TestUser(TestCase):
    def setUp(self):
        self.user = User(name="test name",
                         user_type="student")
        self.serialized_user = UserSerializer(self.user)

    def test_user_serialize(self):
        data = self.serialized_user.data
        assert isinstance(data, dict)
        assert len(data) == 2
        assert isinstance(data['name'], str)
        assert isinstance(data['user_type'], str)