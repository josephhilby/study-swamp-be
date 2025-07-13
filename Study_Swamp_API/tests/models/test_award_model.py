from django.test import TestCase
from Study_Swamp_API.models import Award
from Study_Swamp_API.tests.factories import AwardFactory, UserFactory


class AwardModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.award = AwardFactory(user=self.user)

    def test_award_instance(self):
        self.assertIsInstance(self.award, Award)

    def test_award_state(self):
        assert self.award.user == self.user
