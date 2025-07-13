from django.test import TestCase
from Study_Swamp_API.models import Meeting
from Study_Swamp_API.tests.factories import MeetingFactory


class MeetingModelTests(TestCase):
    def setUp(self):
        self.meeting = MeetingFactory(name='test')

    def test_meeting_instance(self):
        self.assertIsInstance(self.meeting, Meeting)

    def test_meeting_state(self):
        assert self.meeting.name == 'test'
