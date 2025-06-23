from rest_framework import serializers
from .models import User, Group, Member, Meeting, Attendee, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'user_type']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ['user', 'group']

class MeetingSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Meeting
        fields = ['name', 'group']

class AttendeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    meeting = MeetingSerializer(read_only=True)

    class Meta:
        model = Attendee
        fields = ['user', 'meeting']