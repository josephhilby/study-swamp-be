from django.test import TestCase
from Study_Swamp_API.models import Member
from Study_Swamp_API.tests.factories import UserFactory, MemberFactory


class MemberModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.member = MemberFactory(user=self.user)

    def test_member_instance(self):
        self.assertIsInstance(self.member, Member)

    def test_member_state(self):
        assert self.member.user == self.user
