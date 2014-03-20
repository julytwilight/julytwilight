# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.db import DateTimeModel


class User(AbstractUser):

    avatar = models.CharField(max_length=255, blank=True)
    dreams = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    followers = models.PositiveIntegerField(default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Account(DateTimeModel):

    user         = models.ForeignKey(User)
    link_type    = models.CharField(max_length=10)
    link_account = models.CharField(max_length=100)
    avatar       = models.CharField(max_length=255)
    avatar_large = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    expires_in   = models.CharField(max_length=255)