import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import AttendeeViewSet
from Study_Swamp_API.tests.factories import AttendeeFactory, UserFactory

class AttendeeViewTests(TestCase):
    def test_attendee_get_one(self):
        user = UserFactory(username='test', password='password')
        attendee = AttendeeFactory(user=user)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/attendees/{attendee.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = AttendeeViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=attendee.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 9
        assert response.data['user'] == user.pk
        assert response.data['meeting'] == attendee.meeting.pk
        assert response.data['rsvp_type'] == attendee.rsvp_type
        assert response.data['checked_in'] == attendee.checked_in
        assert response.data['creator'] == attendee.creator
        assert response.data['editor'] == attendee.editor

    def test_attendee_get_many(self):
        user = UserFactory(username='test', password='password')
        AttendeeFactory.create_batch(3)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/attendees/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = AttendeeViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 3
