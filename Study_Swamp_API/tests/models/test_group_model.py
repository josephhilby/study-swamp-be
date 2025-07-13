from django.test import TestCase
from Study_Swamp_API.models import Group
from Study_Swamp_API.tests.factories import GroupFactory


class GroupModelTests(TestCase):
    def setUp(self):
        self.group = GroupFactory(name='test')

    def test_group_instance(self):
        self.assertIsInstance(self.group, Group)

    def test_group_state(self):
        assert self.group.name == "test"
