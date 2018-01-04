from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from django.conf import settings

MAX_HRM = 300
MAX_COUNT_HRM_ZONES = 10
HrmField = models.PositiveSmallIntegerField
UserModel = settings.AUTH_USER_MODEL


class HrmProfile(models.Model):
    lactate = HrmField(
        blank=True, null=True, validators=[MaxValueValidator(MAX_HRM)])
    maximum = HrmField(validators=[MaxValueValidator(MAX_HRM)])
    zones = ArrayField(
        HrmField(validators=[MaxValueValidator(MAX_HRM)]),
        size=MAX_COUNT_HRM_ZONES)


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    hrm_profile = models.OneToOneField(HrmProfile, on_delete=models.CASCADE)
    friends = models.ManyToManyField(
        UserModel,
        verbose_name='Friends',
        blank=True,
        related_name='friends')
    about = models.TextField(max_length=250, blank=True)
    birth_data = models.DateField(blank=True, null=True)
    since = models.DateField(
        blank=True, auto_now=True, verbose_name='Registered since')
    web_page = models.URLField(
        max_length=100, verbose_name='Personal page', blank=True, null=True)
