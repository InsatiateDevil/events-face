import uuid

from django.db import models


class Venue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, verbose_name="Название места проведения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место проведения"
        verbose_name_plural = "Места проведения"


class VenueEvent(models.Model):
    class StatusChoices(models.TextChoices):
        OPEN = "open", "open"
        CLOSED = "closed", "closed"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    date = models.DateTimeField(verbose_name="Дата проведения мероприятия")
    status = models.CharField(
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN,
        verbose_name="Статус мероприятия",
    )
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="Площадка проведения мероприятия",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятие"
