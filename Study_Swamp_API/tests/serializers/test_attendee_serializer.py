from django.test import TestCase
from Study_Swamp_API.tests.factories import AttendeeFactory, UserFactory, MeetingFactory
from Study_Swamp_API.serializers import AttendeeSerializer


class TestSerializerAttendee(TestCase):
    def setUp(self):
        self.attendee = AttendeeFactory()
        self.serialized_attendee = AttendeeSerializer(self.attendee)

    def test_attendee_serialize(self):
        data = self.serialized_attendee.data
        assert isinstance(data, dict)
        assert len(data) == 9
        assert isinstance(data['user'], int)
        assert isinstance(data['meeting'], int)
        assert isinstance(data['rsvp_type'], int)
        assert isinstance(data['checked_in'], bool)
        assert isinstance(data['creator'], bool)
        assert isinstance(data['editor'], bool)

    def test_attendee_create(self):
        user = UserFactory()
        meeting = MeetingFactory()
        assert user.points == 0

        data = {
            'user': user.id,
            'group': meeting.id,
        }
        attendee = AttendeeSerializer(data=data)
        assert attendee.is_valid(), attendee.errors
        attendee.save()
        user.refresh_from_db()
        assert user.points == 150
