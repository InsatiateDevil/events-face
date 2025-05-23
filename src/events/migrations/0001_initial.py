# Generated by Django 5.2 on 2025-04-11 13:41

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Venue",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, verbose_name="Название места проведения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Место проведения",
                "verbose_name_plural": "Места проведения",
            },
        ),
        migrations.CreateModel(
            name="VenueEvent",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, verbose_name="Название мероприятия"
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(verbose_name="Дата проведения мероприятия"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("open", "Открыто"), ("closed", "Закрыто")],
                        default="open",
                        verbose_name="Статус мероприятия",
                    ),
                ),
                (
                    "venue",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="events.venue",
                        verbose_name="Площадка проведения мероприятия",
                    ),
                ),
            ],
            options={
                "verbose_name": "Мероприятие",
                "verbose_name_plural": "Мероприятие",
            },
        ),
    ]
