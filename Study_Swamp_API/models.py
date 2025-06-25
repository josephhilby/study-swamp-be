from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        app_label = 'Study_Swamp_API'

    points = models.IntegerField(default=0)


class Location(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    building = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Group(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Member(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='members', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='members', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.BooleanField(default=False)
    editor = models.BooleanField(default=False)


class Meeting(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    group = models.ForeignKey(Group, related_name='meetings', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='meetings', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attendee(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    class RSVP(models.IntegerChoices):
        PENDING = 0, 'Pending'
        ACCEPTED = 1, 'Accepted'
        DECLINED = 2, 'Declined'

    user = models.ForeignKey(User, related_name='attendees', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, related_name='attendees', on_delete=models.CASCADE)
    rsvp = models.IntegerField(choices=RSVP.choices, default=RSVP.PENDING)
    creator = models.BooleanField(default=False)
    editor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Badge(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    class BadgeType(models.IntegerChoices):
        WELCOME = 1, 'Welcome'
        ACHIEVER = 2, 'Achiever'
        EXPERT = 3, 'Expert'

    badge_type = models.IntegerField(choices=BadgeType.choices)
    created_at = models.DateTimeField(auto_now_add=True)


class Award(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='awards', on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, related_name='awards', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class MeetingComment(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='meeting_comments', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupComment(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='group_comments', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='group_comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
