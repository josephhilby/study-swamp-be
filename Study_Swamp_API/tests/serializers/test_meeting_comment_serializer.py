from django.test import TestCase
from Study_Swamp_API.tests.factories import MeetingCommentFactory
from Study_Swamp_API.serializers import MeetingCommentSerializer


class TestSerializerMeetingComment(TestCase):
    def setUp(self):
        self.comment = MeetingCommentFactory()
        self.serialized_comment = MeetingCommentSerializer(self.comment)

    def test_meeting_comment_serialize(self):
        data = self.serialized_comment.data
        assert isinstance(data, dict)
        assert len(data) == 6
        assert isinstance(data['user'], int)
        assert isinstance(data['meeting'], int)
        assert isinstance(data['text'], str)
