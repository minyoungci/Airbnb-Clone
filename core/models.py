from django.db import models


class TimeStampedModel(models.Model):

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
