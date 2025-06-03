from django.db import models

class User(models.Model):
    class Meta:
        app_label = 'Study_Swamp_API'

    class UserTypes(models.IntegerChoices):
        STUDENT = 1, 'Student',
        ADMIN = 2, 'Admin'

    name = models.CharField(max_length=50)
    user_type = models.IntegerField(
        default=UserTypes.STUDENT,
        choices=UserTypes.choices
    )