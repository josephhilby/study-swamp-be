from django.test import TestCase
from Study_Swamp_API.tests.factories import MemberFactory, UserFactory, GroupFactory
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

    def test_member_create(self):
        user = UserFactory()
        group = GroupFactory()
        assert user.points == 0

        data = {
            'user': user.id,
            'group': group.id,
        }
        member = MemberSerializer(data=data)
        assert member.is_valid(), member.errors
        member.save()
        user.refresh_from_db()
        assert user.points == 50
