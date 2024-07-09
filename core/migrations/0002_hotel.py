# Generated by Django 5.0.3 on 2024-07-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
