# Generated by Django 2.2.7 on 2019-11-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alignmentapp', '0015_userprofile_exclude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanrelevancejudgment',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
