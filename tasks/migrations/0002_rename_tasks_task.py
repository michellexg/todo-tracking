# Generated by Django 4.1.4 on 2022-12-07 00:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="tasks",
            new_name="Task",
        ),
    ]
