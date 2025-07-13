from django.test import TestCase
from Study_Swamp_API.tests.factories import UserFactory
from Study_Swamp_API.serializers import UserSerializer


class TestSerializerUser(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.serialized_user = UserSerializer(self.user)

    def test_user_serialize(self):
        data = self.serialized_user.data
        assert isinstance(data, dict)
        assert len(data) == 6
        assert isinstance(data['username'], str)
        assert isinstance(data['email'], str)
        assert isinstance(data['first_name'], str)
        assert isinstance(data['last_name'], str)
