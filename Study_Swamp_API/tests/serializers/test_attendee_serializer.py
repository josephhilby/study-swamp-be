from django.test import TestCase
from Study_Swamp_API.tests.factories import AttendeeFactory
from Study_Swamp_API.serializers import AttendeeSerializer


class TestSerializerAttendee(TestCase):
    def setUp(self):
        self.attendee = AttendeeFactory()
        self.serialized_attendee = AttendeeSerializer(self.attendee)

    def test_meeting_serialize(self):
        data = self.serialized_attendee.data
        assert isinstance(data, dict)
        assert len(data) == 9
        assert isinstance(data['user'], int)
        assert isinstance(data['meeting'], int)
        assert isinstance(data['rsvp_type'], int)
        assert isinstance(data['checked_in'], bool)
        assert isinstance(data['creator'], bool)
        assert isinstance(data['editor'], bool)
