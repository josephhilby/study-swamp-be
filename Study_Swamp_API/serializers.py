from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone
from .models import *


def award_points(user, points):
    user.points += points
    user.save(update_fields=['points'])


def award_points_time_delay(user, model, delay, points):
    """
    Awards points and adds a time delay to avoid farming.
    """
    time_threshold = timezone.now() + timedelta(seconds=delay)
    recent = model.objects.filter(user=user, created_at__gt=time_threshold)
    if not recent.exists():
        award_points(user, points)


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
    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        award_points_time_delay(user, Member, 30, 50)
        member = super().create(validated_data)
        return member


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        meeting = super().create(validated_data)
        Attendee.objects.create(
            user=user,
            meeting=meeting,
            creator=True
        )
        return meeting


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        creator = validated_data['creator']
        if creator:
            award_points_time_delay(user, Attendee, 30, 150)
        attendee = super().create(validated_data)
        return attendee

    def update(self, instance, validated_data):
        user = validated_data['user']
        checked_in = validated_data['checked_in']

        if checked_in:
            award_points_time_delay(user, Attendee, 30, 100)

        update = super().update(instance, validated_data)
        return update


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class MeetingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingComment
        fields = '__all__'


class GroupCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupComment
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        award_points_time_delay(user, GroupComment, 30, 10)
        comment = super().create(validated_data)
        return comment
