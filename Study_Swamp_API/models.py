from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        app_label = 'Study_Swamp_API'

    '''
    POINTS:
      - 5 for joining a group
      - 5 for RSVP 'ACCEPTED' to a meeting
      - 10 for marking checked_in to a meeting
    '''
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

    class DEPT(models.TextChoices):
        MAS = 'MAS', 'MAS'
        CEN = 'CEN', 'CEN'
        COP = 'COP', 'COP'

    name = models.CharField(max_length=50)
    department = models.TextField(choices=DEPT.choices, default=DEPT.MAS)
    class_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Member(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='members', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='members', on_delete=models.CASCADE)
    creator = models.BooleanField(default=False)
    editor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meeting(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    group = models.ForeignKey(Group, related_name='meetings', on_delete=models.CASCADE, null=True, blank=True)
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
    rsvp_type = models.IntegerField(choices=RSVP.choices, default=RSVP.PENDING)
    checked_in = models.BooleanField(default=False)
    creator = models.BooleanField(default=False)
    editor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Award(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    class BadgeType(models.IntegerChoices):
        EGG_TOOTH = 0, 'Egg Tooth'         # for creating an account
        FIRST_SPLASH = 1, 'First Splash'   # for joining your first group
        SNAP_TO_IT = 2, 'Snap to It!'      # for marking checked_in at first meeting
        TAILGATOR = 3, 'TailGATOR'         # for marking checked_in at a meeting that has no associated group
        GATOR_DONE = 4, 'Gator Done'       # for marking checked_in at 5 meetings
        CHOMP_CHAMP = 5, 'Chomp Champ'     # for getting 100 points


    user = models.ForeignKey(User, related_name='awards', on_delete=models.CASCADE)
    badge_type = models.IntegerField(choices=BadgeType.choices)
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
