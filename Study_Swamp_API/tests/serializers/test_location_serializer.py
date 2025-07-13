from django.test import TestCase
from Study_Swamp_API.tests.factories import LocationFactory
from Study_Swamp_API.serializers import LocationSerializer


class TestSerializerLocation(TestCase):
    def setUp(self):
        self.location = LocationFactory()
        self.serialized_location = LocationSerializer(self.location)

    def test_location_serialize(self):
        data = self.serialized_location.data
        assert isinstance(data, dict)
        assert len(data) == 7
        assert isinstance(data['building'], str)
        assert isinstance(data['room'], str)
        assert isinstance(data['latitude'], float)
        assert isinstance(data['longitude'], float)
