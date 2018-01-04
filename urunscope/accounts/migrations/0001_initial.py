# Generated by Django 2.0 on 2018-01-04 23:07

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HrmProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lactate', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(300)])),
                ('maximum', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(300)])),
                ('zones', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(300)]), blank=True, null=True, size=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hrm_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, max_length=250)),
                ('birth_data', models.DateField(blank=True, null=True)),
                ('since', models.DateField(auto_now=True, verbose_name='Registered since')),
                ('web_page', models.URLField(blank=True, max_length=100, null=True, verbose_name='Personal page')),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL, verbose_name='Friends')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
