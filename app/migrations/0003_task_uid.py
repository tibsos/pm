# Generated by Django 5.0.3 on 2024-03-25 14:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userwithtasks_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]