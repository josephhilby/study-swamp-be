from django.test import TestCase
from Study_Swamp_API.tests.factories import GroupFactory
from Study_Swamp_API.serializers import GroupSerializer


class TestSerializerGroup(TestCase):
    def setUp(self):
        self.group = GroupFactory()
        self.serialized_group = GroupSerializer(self.group)

    def test_group_serialize(self):
        data = self.serialized_group.data
        assert isinstance(data, dict)
        assert len(data) == 6
        assert isinstance(data['name'], str)
        assert isinstance(data['department'], str)
        assert isinstance(data['class_number'], int)
