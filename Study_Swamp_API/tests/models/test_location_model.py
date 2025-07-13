from django.test import TestCase
from Study_Swamp_API.models import Location
from Study_Swamp_API.tests.factories import LocationFactory


class LocationModelTests(TestCase):
    def setUp(self):
        self.location = LocationFactory(building='building')

    def test_location_instance(self):
        self.assertIsInstance(self.location, Location)

    def test_location_state(self):
        assert self.location.building == "building"
