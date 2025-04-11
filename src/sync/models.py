from django.db import models
from django.utils import timezone


class SyncResult(models.Model):
    sync_date = models.DateTimeField(default=timezone.now)
    new_events_counter = models.IntegerField(default=0)
    updated_events_counter = models.IntegerField(default=0)

    def __str__(self):
        return (
            f"Синхронизировано мероприятий: {self.sync_date}"
            f"Загружено новых мероприятий: {self.new_events_counter},"
            f"Обновлено мероприятий: {self.updated_events_counter}"
        )

    class Meta:
        verbose_name = "Результат синхронизации"
        verbose_name_plural = "Результаты синхронизации"
