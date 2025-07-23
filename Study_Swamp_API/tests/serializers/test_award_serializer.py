from django.test import TestCase
from rest_framework.test import APIClient
from Study_Swamp_API.models import Award, User, Attendee
from Study_Swamp_API.tests.factories import AwardFactory, UserFactory, MeetingFactory, AttendeeFactory, GroupFactory, \
    MemberFactory
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

        awards = Award.objects.filter(user=user)
        assert Award.objects.count() == 1

        response = client.post('/api/v1/groups/', {
            'name': 'group',
            'department': 'MAS',
            'class_number': 1234
        }, format='json')

        assert response.status_code == 201

        user.refresh_from_db()
        award = Award.objects.get(user=user)
        assert award.badge_type == Award.BadgeType.FIRST_SPLASH

    def test_award_snap_to_it(self):
        user = UserFactory()
        meeting = MeetingFactory()
        attendee = AttendeeFactory(
            user=user,
            meeting=meeting,
            checked_in=False
        )

        client = APIClient()
        client.force_authenticate(user=user)

        assert attendee.checked_in == False
        assert Award.objects.count() == 1

        response = client.patch(f"/api/v1/attendees/{attendee.id}/", {
            'checked_in': True
        }, format='json')

        assert response.status_code == 200

        user.refresh_from_db()
        awards = Award.objects.filter(user=user)
        assert any(award.badge_type == Award.BadgeType.SNAP_TO_IT for award in awards)

    def test_award_tail_gator(self):
        user = UserFactory()
        meeting = MeetingFactory(group=None)
        attendee = AttendeeFactory(
            user=user,
            meeting=meeting,
            checked_in=False
        )

        client = APIClient()
        client.force_authenticate(user=user)

        assert attendee.checked_in == False
        assert Award.objects.count() == 1

        response = client.patch(f"/api/v1/attendees/{attendee.id}/", {
            'checked_in': True
        }, format='json')

        assert response.status_code == 200

        user.refresh_from_db()
        awards = Award.objects.filter(user=user)
        assert any(award.badge_type == Award.BadgeType.TAILGATOR for award in awards)

    def test_award_gator_done(self):
        user = UserFactory()
        meeting = MeetingFactory(group=None)
        AttendeeFactory.create_batch(4, user=user, checked_in=True)
        attendee = AttendeeFactory(
            user=user,
            meeting=meeting,
            checked_in=False
        )

        client = APIClient()
        client.force_authenticate(user=user)

        assert attendee.checked_in == False
        assert Award.objects.count() == 1

        response = client.patch(f"/api/v1/attendees/{attendee.id}/", {
            'checked_in': True
        }, format='json')

        assert response.status_code == 200

        user.refresh_from_db()
        awards = Award.objects.filter(user=user)
        assert any(award.badge_type == Award.BadgeType.GATOR_DONE for award in awards)

    def test_award_chomp_champ(self):
        user = UserFactory(points=990)
        group = GroupFactory()
        member = MemberFactory(user=user, group=group)

        client = APIClient()
        client.force_authenticate(user=user)

        assert Award.objects.count() == 1

        response = client.post('/api/v1/group_comments/', {
            'user': user.id,
            'group': group.id,
            'text': 'testing'
        }, format='json')

        assert response.status_code == 201

        user.refresh_from_db()
        awards = Award.objects.filter(user=user)
        assert any(award.badge_type == Award.BadgeType.CHOMP_CHAMP for award in awards)
