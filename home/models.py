# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    mmsi = models.IntegerField(null=True, blank=True)
    lon = models.TextField(max_length=255, null=True, blank=True)
    lat = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Ais_Msgtype_1(models.Model):

    #__Ais_Msgtype_1_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    msg_type = models.IntegerField(null=True, blank=True)
    mmsi = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    turn = models.TextField(max_length=255, null=True, blank=True)
    speed = models.TextField(max_length=255, null=True, blank=True)
    accuracy = models.TextField(max_length=255, null=True, blank=True)
    lon = models.TextField(max_length=255, null=True, blank=True)
    lat = models.TextField(max_length=255, null=True, blank=True)
    course = models.TextField(max_length=255, null=True, blank=True)
    heading = models.TextField(max_length=255, null=True, blank=True)
    second = models.TextField(max_length=255, null=True, blank=True)
    maneuver = models.TextField(max_length=255, null=True, blank=True)
    spare_1 = models.TextField(max_length=255, null=True, blank=True)
    raim = models.TextField(max_length=255, null=True, blank=True)
    radio = models.TextField(max_length=255, null=True, blank=True)

    #__Ais_Msgtype_1_FIELDS__END

    class Meta:
        verbose_name        = _("Ais_Msgtype_1")
        verbose_name_plural = _("Ais_Msgtype_1")



#__MODELS__END
