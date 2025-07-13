import base64
from dateutil import parser

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import MeetingViewSet
from Study_Swamp_API.tests.factories import MeetingFactory, UserFactory

class MeetingViewTests(TestCase):
    def test_meeting_get_one(self):
        user = UserFactory(username='test', password='password')
        meeting = MeetingFactory()

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/meetings/{meeting.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = MeetingViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=meeting.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 8
        assert response.data['group'] == meeting.group.pk
        assert response.data['location'] == meeting.location.pk
        assert parser.isoparse(response.data["start_time"]) == meeting.start_time
        assert parser.isoparse(response.data["end_time"]) == meeting.end_time

    def test_meeting_get_many(self):
        user = UserFactory(username='test', password='password')
        MeetingFactory.create_batch(3)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/meetings/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = MeetingViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 3
