import pytest
import json
import base64
from django.test import TestCase, Client
from Study_Swamp_API.tests.factories import UserFactory

class UserIndexTests(TestCase):
    def test_user_index(self):
        UserFactory(username='test')
        UserFactory.create_batch(2)

        credentials = base64.b64encode(b'test:password').decode('utf-8')
        auth_header = f'Basic {credentials}'

        client = Client()
        response = client.get(
            "/api/v1/users/",
            HTTP_AUTHORIZATION=auth_header
        )

        assert response.status_code == 200
        content = json.loads(response.content)
        assert isinstance(content, dict)
        assert len(content) == 1
        assert isinstance(content['data'], list)
        assert len(content['data']) == 3

        for entry in content['data']:
          assert isinstance(entry, dict)
          assert len(entry) == 3
          assert isinstance(entry['type'], str)
          assert entry['type'] == 'User'
          assert isinstance(entry['id'], str)
          assert isinstance(entry['attributes'], dict)
          assert len(entry['attributes']) == 5
          assert isinstance(entry['attributes']['username'], str)
          assert isinstance(entry['attributes']['email'], str)
          assert isinstance(entry['attributes']['first_name'], str)
          assert isinstance(entry['attributes']['last_name'], str)
          assert isinstance(entry['attributes']['points'], int)
