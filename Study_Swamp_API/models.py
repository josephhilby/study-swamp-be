from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'Study_Swamp_API'