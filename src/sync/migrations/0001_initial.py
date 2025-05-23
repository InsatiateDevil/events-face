# Generated by Django 5.2 on 2025-04-11 12:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SyncResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sync_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("new_events_counter", models.IntegerField(default=0)),
                ("updated_events_counter", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Результат синхронизации",
                "verbose_name_plural": "Результаты синхронизации",
            },
        ),
    ]
