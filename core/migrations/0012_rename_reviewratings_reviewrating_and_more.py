# Generated by Django 5.0.3 on 2024-09-16 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_merge_0008_reviewratings_0010_hotel_officer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewRatings',
            new_name='ReviewRating',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='officer',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
