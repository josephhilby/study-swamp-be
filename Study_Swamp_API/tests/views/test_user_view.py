import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import UserViewSet
from Study_Swamp_API.tests.factories import UserFactory

class UserViewTests(TestCase):
    def test_user_get_one(self):
        user = UserFactory(username='test', password='password')

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/user/{user.pk}",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = UserViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=user.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 5
        assert response.data['username'] == user.username
        assert response.data['email'] == user.email
        assert response.data['first_name'] == user.first_name
        assert response.data['last_name'] == user.last_name
        assert response.data['points'] == user.points
