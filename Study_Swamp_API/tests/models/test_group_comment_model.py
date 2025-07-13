from django.test import TestCase
from Study_Swamp_API.models import GroupComment
from Study_Swamp_API.tests.factories import GroupCommentFactory, UserFactory


class GroupCommentModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.comment = GroupCommentFactory(user=self.user)

    def test_group_comment_instance(self):
        self.assertIsInstance(self.comment, GroupComment)

    def test_group_comment_state(self):
        assert self.comment.user == self.user
