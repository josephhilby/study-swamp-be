from django.test import TestCase
from Study_Swamp_API.models import Attendee
from Study_Swamp_API.tests.factories import AttendeeFactory, UserFactory


class AttendeeModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.attendee = AttendeeFactory(user=self.user)

    def test_attendee_instance(self):
        self.assertIsInstance(self.attendee, Attendee)

    def test_attendee_state(self):
        assert self.attendee.user == self.user
