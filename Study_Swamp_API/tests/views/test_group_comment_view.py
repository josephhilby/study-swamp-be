import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import GroupCommentViewSet
from Study_Swamp_API.tests.factories import GroupCommentFactory, UserFactory

class GroupCommentViewTests(TestCase):
    def test_group_comment_get_one(self):
        user = UserFactory(username='test', password='password')
        comment = GroupCommentFactory(user=user)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/meeting_comments/{comment.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = GroupCommentViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=comment.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 6
        assert response.data['user'] == user.pk
        assert response.data['group'] == comment.group.pk
        assert response.data['text'] == comment.text

    def test_group_comment_get_many(self):
        user = UserFactory(username='test', password='password')
        GroupCommentFactory.create_batch(3)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/meeting_comments/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = GroupCommentViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 3
