# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from ahead.utils.db import DateTimeModel

class Dream(DateTimeModel):

    user      = models.ForeignKey("ahead.User", unique_for_date="create_at")
    text      = models.TextField()
    comments  = models.PositiveIntegerField(default=0)
    recommend = models.BooleanField(default=False)
    private   = models.BooleanField(default=False)
    status    = models.PositiveSmallIntegerField(default=0)
    point     = models.PositiveIntegerField(default=0)
    date      = models.DateTimeField(default=timezone.now().date())

    class Meta:
        app_label = 'dreams'


class Comment(DateTimeModel):

    user    = models.ForeignKey("ahead.User")
    dream   = models.ForeignKey(Dream)
    text    = models.TextField()
    status  = models.PositiveSmallIntegerField(default=0)