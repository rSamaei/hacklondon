# Generated by Django 5.1.6 on 2025-03-01 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0002_university_society_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='societies.university'),
        ),
    ]
