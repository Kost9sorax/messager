from django.db import models


class Messages(models.Model):
    user_id = models.IntegerField('User')
    message = models.CharField('Message', max_length=255)
    status = models.CharField('Status', max_length=255, default='review', null=True)
