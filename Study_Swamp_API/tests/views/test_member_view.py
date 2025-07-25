import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import MemberViewSet
from Study_Swamp_API.tests.factories import MemberFactory, UserFactory

class MemberViewTests(TestCase):
    def test_member_get_one(self):
        user = UserFactory(username='test', password='password')
        member = MemberFactory(user=user)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/members/{member.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = MemberViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=member.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 8
        assert response.data['user'] == user.pk
        assert response.data['group'] == member.group.pk
        assert response.data['creator'] == member.creator
        assert response.data['editor'] == member.editor
        assert response.data['granted_awards'] == []

    def test_member_get_many(self):
        user = UserFactory(username='test', password='password')
        MemberFactory.create_batch(3)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/members/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = MemberViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 3
