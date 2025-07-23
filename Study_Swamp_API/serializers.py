from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone
from .models import *


def grant_award(user, award):
    Award.objects.get_or_create(
        user=user,
        badge_type=award
    )


def award_points(user, points):
    total = user.points + points
    needs_chomp = total >= 1000 > user.points

    user.points = total
    user.save(update_fields=['points'])

    if needs_chomp:
        grant_award(user, Award.BadgeType.CHOMP_CHAMP)


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
        grant_award(user, Award.BadgeType.EGG_TOOTH)
        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        group = super().create(validated_data)
        data = {
            'user': user.id,
            'group': group.id,
            'creator': True
        }

        serialize = MemberSerializer(
            data=data,
            context={**self.context, 'internal': True}
        )

        serialize.is_valid(raise_exception=True)
        serialize.save()
        return group


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['creator']

    def create(self, validated_data):
        user = validated_data['user']
        grant_award(user, Award.BadgeType.FIRST_SPLASH)
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
        data = {
            'user': user.id,
            'meeting': meeting.id,
            'creator': True
        }

        serialize = AttendeeSerializer(
            data=data,
            context={**self.context, 'internal': True}
        )

        serialize.is_valid(raise_exception=True)
        serialize.save()
        return meeting


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'
        read_only_fields = ['creator']

    def create(self, validated_data):
        user = validated_data['user']
        creator = self.initial_data.get('creator', False)

        is_creator = creator is True and self.context.get('internal', False)
        if is_creator:
            award_points_time_delay(user, Attendee, 30, 150)

        validated_data['creator'] = is_creator
        attendee = super().create(validated_data)
        return attendee

    def update(self, instance, validated_data):
        user = instance.user
        checked_in = validated_data.get('checked_in', instance.checked_in)

        just_checked_in = checked_in and not instance.checked_in
        update = super().update(instance, validated_data)

        if just_checked_in:
            award_points_time_delay(user, Attendee, 30, 100)
            grant_award(user, Award.BadgeType.SNAP_TO_IT)

            if not instance.meeting.group_id:
                grant_award(user, Award.BadgeType.TAILGATOR)

            checked_in_count = Attendee.objects.filter(user=user, checked_in=True).count()
            if checked_in_count == 5:
                grant_award(user, Award.BadgeType.GATOR_DONE)

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
