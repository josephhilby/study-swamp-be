from django.test import TestCase
from Study_Swamp_API.tests.factories import AwardFactory
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
