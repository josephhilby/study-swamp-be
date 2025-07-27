import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import GroupViewSet
from Study_Swamp_API.tests.factories import GroupFactory, UserFactory

class GroupViewTests(TestCase):
    def test_group_get_one(self):
        user = UserFactory(username='test', password='password')
        group = GroupFactory()

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/groups/{group.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = GroupViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=group.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 7
        assert response.data['name'] == group.name
        assert response.data['department'] == group.department
        assert response.data['class_number'] == group.class_number
        assert response.data['granted_awards'] == []

    def test_group_get_many(self):
        user = UserFactory(username='test', password='password')
        GroupFactory.create_batch(3)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/groups/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = GroupViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 3
