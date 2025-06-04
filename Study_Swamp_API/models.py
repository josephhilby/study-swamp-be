from django.db import models

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