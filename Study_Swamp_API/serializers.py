from rest_framework import serializers
from .models import User, Location, Group, Member, Meeting, Attendee, Badge, Award, MeetingComment, GroupComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'points', 'is_superuser']
        extra_kwargs = {
            'is_superuser': {'read_only': True},
            'points': {'read_only': True},
            'password': {'write_only': True},
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request and not request.user.is_superuser:
            rep.pop('is_superuser', None)
        return rep

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Member
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'


class AttendeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    meeting = MeetingSerializer(read_only=True)

    class Meta:
        model = Attendee
        fields = '__all__'


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    badge = BadgeSerializer(read_only=True)

    class Meta:
        model = Award
        fields = '__all__'


class MeetingCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    meeting = MeetingSerializer(read_only=True)

    class Meta:
        model = MeetingComment
        fields = '__all__'


class GroupCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = GroupComment
        fields = '__all__'
