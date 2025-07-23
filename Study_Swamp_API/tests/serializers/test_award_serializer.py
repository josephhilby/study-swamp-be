from django.test import TestCase
from rest_framework.test import APIClient
from Study_Swamp_API.models import Award, User
from Study_Swamp_API.tests.factories import AwardFactory, UserFactory
from Study_Swamp_API.serializers import AwardSerializer


class TestSerializerAward(TestCase):
    def setUp(self):
        self.award = AwardFactory()
        self.serialized_award = AwardSerializer(self.award)

    def test_award_serialize(self):
        data = self.serialized_award.data
        assert isinstance(data, dict)
        assert len(data) == 4
        assert isinstance(data['user'], int)
        assert isinstance(data['badge_type'], int)

    def test_award_egg_tooth(self):
        client = APIClient()

        response = client.post('/api/v1/users/', {
            'first_name': 'first',
            'last_name': 'last',
            'username': 'cool-user-name',
            'email': 'first.last@email.com',
            'password': 'password',
            'points': 0,
            'is_superuser': False
        }, format='json')

        assert response.status_code == 201

        user = User.objects.get(username='cool-user-name')
        award = Award.objects.get(user=user)
        assert award.badge_type == Award.BadgeType.EGG_TOOTH

    def test_award_first_splash(self):
        user = UserFactory()
        client = APIClient()
        client.force_authenticate(user=user)

        response = client.post('/api/v1/groups/', {
            'name': 'group',
            'department': 'MAS',
            'class_number': 1234
        }, format='json')

        assert response.status_code == 201, response.data

        user.refresh_from_db()
        award = Award.objects.get(user=user)
        assert award.badge_type == Award.BadgeType.FIRST_SPLASH

    # TO-DO: Test for Snap to It!

    # TO-DO: Test for TailGATOR

    # TO-DO: Test for Gator Done

    # TO-DO: Test for Chomp Champ

