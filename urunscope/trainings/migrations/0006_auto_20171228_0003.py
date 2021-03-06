# Generated by Django 2.0 on 2017-12-28 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0005_training_hrm'),
    ]

    operations = [
        migrations.CreateModel(
            name='HrmSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lowest', models.PositiveSmallIntegerField()),
                ('highest', models.PositiveSmallIntegerField()),
                ('avarage', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='training',
            name='hrm_summary',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainings.HrmSummary'),
        ),
    ]
