import base64

from django.test import TestCase, RequestFactory
from Study_Swamp_API.views import AwardViewSet
from Study_Swamp_API.tests.factories import AwardFactory, UserFactory

class AwardViewTests(TestCase):
    def test_award_get_one(self):
        user = UserFactory(username='test', password='password')
        award = AwardFactory(user=user)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/awards/{award.pk}/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = AwardViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=award.pk)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 4
        assert response.data['user'] == user.pk
        assert response.data['badge_type'] == award.badge_type

    def test_award_get_many(self):
        user = UserFactory(username='test', password='password')
        AwardFactory.create_batch(3, user=user)
        AwardFactory.create_batch(2)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        request = RequestFactory().get(
            f"api/v1/awards/",
            HTTP_AUTHORIZATION=auth_header
        )

        request.user = user

        view = AwardViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()

        assert response.status_code == 200
        assert len(response.data) == 3
