from django.test import TestCase
from Study_Swamp_API.tests.factories import GroupCommentFactory
from Study_Swamp_API.serializers import GroupCommentSerializer


class TestSerializerGroupComment(TestCase):
    def setUp(self):
        self.comment = GroupCommentFactory()
        self.serialized_comment = GroupCommentSerializer(self.comment)

    def test_group_comment_serialize(self):
        data = self.serialized_comment.data
        assert isinstance(data, dict)
        assert len(data) == 6
        assert isinstance(data['user'], int)
        assert isinstance(data['group'], int)
        assert isinstance(data['text'], str)
