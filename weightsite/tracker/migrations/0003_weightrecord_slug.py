# Generated by Django 5.0.1 on 2024-01-24 15:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_weightrecord_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weightrecord',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
