import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import LocationViewSet
from Study_Swamp_API.tests.factories import LocationFactory, UserFactory

class LocationViewTests(TestCase):
    def test_location_get_one(self):
        user = UserFactory(username='test', password='password')
        location = LocationFactory()

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/locations/{location.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = LocationViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=location.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 7
        assert response.data['building'] == location.building
        assert response.data['room'] == location.room
        assert response.data['latitude'] == float(location.latitude)
        assert response.data['longitude'] == float(location.longitude)

    def test_location_get_many(self):
        user = UserFactory(username='test', password='password')
        location = LocationFactory()

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/locations/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = LocationViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=location.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 7
        assert response.data['building'] == location.building
        assert response.data['room'] == location.room
        assert response.data['latitude'] == float(location.latitude)
        assert response.data['longitude'] == float(location.longitude)
