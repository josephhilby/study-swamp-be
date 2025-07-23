from django.test import TestCase
from rest_framework.test import APIClient
from Study_Swamp_API.models import Attendee
from Study_Swamp_API.tests.factories import AttendeeFactory, UserFactory, MeetingFactory, GroupFactory, LocationFactory
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

    def test_attendee_auto_create(self):
        user = UserFactory()
        group = GroupFactory()
        location = LocationFactory()
        meeting = MeetingFactory()

        client = APIClient()
        client.force_authenticate(user=user)

        response = client.post('/api/v1/meetings/', {
            'group': group.id,
            'location': location.id,
            'name': meeting.name,
            'start_time': meeting.start_time,
            'end_time': meeting.end_time
        }, format='json')

        assert response.status_code == 201

        attendee = Attendee.objects.get(user=user)
        assert attendee.creator == True
        user.refresh_from_db()
        assert user.points == 150

    def test_attendee_update(self):
        user = UserFactory()
        meeting = MeetingFactory()

        data = {
            'user': user.id,
            'meeting': meeting.id,
            'checked_in': False
        }
        attendee = AttendeeSerializer(data=data)
        assert attendee.is_valid(), attendee.errors
        attendee = attendee.save()

        assert attendee.checked_in == False
        assert user.points == 0

        update = {
            'user': user.id,
            'checked_in': True
        }

        updated_attendee = AttendeeSerializer(
            attendee,
            data=update,
            partial=True
        )

        assert updated_attendee.is_valid(), updated_attendee.errors
        updated_attendee.save()

        user.refresh_from_db()
        assert user.points == 100

