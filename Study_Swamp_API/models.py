from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class User(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    class UserTypes(models.TextChoices):
        STUDENT = 'STUDENT', 'Student',
        ADMIN = 'ADMIN', 'Admin'

    name = models.CharField(max_length=50)
    user_type = models.CharField(
        max_length=10,
        default=UserTypes.STUDENT,
        choices=UserTypes.choices
    )

class Group(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    name = models.CharField(max_length=50)

class Member(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='members', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='members', on_delete=models.CASCADE)

class Meeting(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, related_name='meetings', on_delete=models.CASCADE)

class Attendee(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    user = models.ForeignKey(User, related_name='attendees', on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, related_name='attendees', on_delete=models.CASCADE)

class Comment(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    text = models.TextField()
    entity_id = models.PositiveIntegerField()
    entity_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    entity_object = GenericForeignKey('entity_type', 'entity_id')
