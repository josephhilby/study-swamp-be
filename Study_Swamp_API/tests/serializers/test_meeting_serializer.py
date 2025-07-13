from django.test import TestCase
from Study_Swamp_API.tests.factories import MeetingFactory
from Study_Swamp_API.serializers import MeetingSerializer


class TestSerializerMeeting(TestCase):
    def setUp(self):
        self.meeting = MeetingFactory()
        self.serialized_meeting = MeetingSerializer(self.meeting)

    def test_meeting_serialize(self):
        data = self.serialized_meeting.data
        assert isinstance(data, dict)
        assert len(data) == 8
        assert isinstance(data['group'], int)
        assert isinstance(data['location'], int)
        assert isinstance(data['name'], str)
        assert isinstance(data['start_time'], str)
        assert isinstance(data['start_time'], str)
