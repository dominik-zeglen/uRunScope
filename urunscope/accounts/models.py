from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

MAX_HRM = 300
MAX_COUNT_HRM_ZONES = 10
HrmField = models.PositiveSmallIntegerField
UserModel = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    friends = models.ManyToManyField(
        UserModel, verbose_name='Friends', blank=True, related_name='friends')
    about = models.TextField(max_length=250, blank=True)
    birth_data = models.DateField(blank=True, null=True)
    since = models.DateField(
        blank=True, auto_now=True, verbose_name='Registered since')
    web_page = models.URLField(
        max_length=100, verbose_name='Personal page', blank=True, null=True)

    def __str__(self):
        return self.user.username


class HrmProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='hrm_profile')
    lactate = HrmField(
        blank=True, null=True, validators=[MaxValueValidator(MAX_HRM)])
    maximum = HrmField(
        validators=[MaxValueValidator(MAX_HRM)], blank=True, null=True)
    zones = ArrayField(
        HrmField(validators=[MaxValueValidator(MAX_HRM)]),
        size=MAX_COUNT_HRM_ZONES,
        blank=True,
        null=True)


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=UserModel)
def create_hrm_profile(sender, instance, created, **kwargs):
    if created:
        HrmProfile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_hrm_profile(sender, instance, created, **kwargs):
    instance.hrm_profile.save()
