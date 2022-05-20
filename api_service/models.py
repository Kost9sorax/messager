from django.db import models
from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return list((x.name, x.value) for x in cls)


class StatusTypes(BaseEnum):
    REVIEW = 'review'
    CORRECT = 'correct'
    BLOCKED = 'blocked'


class Messages(models.Model):
    user_id = models.IntegerField('User')
    message = models.CharField('Message', max_length=255)
    token = models.CharField('Token', max_length=500)
    status = models.CharField('Status', max_length=25, default=StatusTypes.REVIEW.value)
