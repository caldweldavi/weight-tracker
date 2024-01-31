# Generated by Django 4.2.9 on 2024-01-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_weightrecord_body_fat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightrecord',
            name='body_fat',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
