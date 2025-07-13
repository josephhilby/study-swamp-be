from django.test import TestCase
from Study_Swamp_API.models import MeetingComment
from Study_Swamp_API.tests.factories import MeetingCommentFactory, UserFactory


class MeetingCommentModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.comment = MeetingCommentFactory(user=self.user)

    def test_meeting_comment_instance(self):
        self.assertIsInstance(self.comment, MeetingComment)

    def test_meeting_comment_state(self):
        assert self.comment.user == self.user
