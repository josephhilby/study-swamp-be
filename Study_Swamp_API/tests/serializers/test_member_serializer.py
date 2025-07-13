from django.test import TestCase
from Study_Swamp_API.tests.factories import MemberFactory
from Study_Swamp_API.serializers import MemberSerializer


class TestSerializerMember(TestCase):
    def setUp(self):
        self.member = MemberFactory()
        self.serialized_member = MemberSerializer(self.member)

    def test_member_serialize(self):
        data = self.serialized_member.data
        assert isinstance(data, dict)
        assert len(data) == 7
        assert isinstance(data['user'], int)
        assert isinstance(data['group'], int)
        assert isinstance(data['creator'], bool)
        assert isinstance(data['editor'], bool)
