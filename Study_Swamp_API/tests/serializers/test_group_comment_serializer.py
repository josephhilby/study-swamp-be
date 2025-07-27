from django.test import TestCase
from Study_Swamp_API.tests.factories import GroupCommentFactory, GroupFactory, UserFactory
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

    def test_group_comment_create(self):
        user = UserFactory()
        group = GroupFactory()
        assert user.points == 0

        data = {
            'user': user.id,
            'group': group.id,
            'text': 'testing'
        }
        comment = GroupCommentSerializer(data=data)
        assert comment.is_valid(), comment.errors
        comment.save()
        user.refresh_from_db()
        assert user.points == 10
