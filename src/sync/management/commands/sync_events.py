from datetime import datetime, timedelta

import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from src.events.models import VenueEvent
from src.sync.models import SyncResult


class Command(BaseCommand):
    help = "Синхронизация событий с сервера"

    def add_arguments(self, parser):
        parser.add_argument(
            "--date", type=str, help="Дата синхронизации в формате YYYY-MM-DD"
        )
        parser.add_argument(
            "--all", action="store_true", help="Синхронизировать все события"
        )

    def handle(self, *args, **options):
        sync_date = options.get("date", None)
        if sync_date is None:
            sync_date = (timezone.now() - timedelta(days=1)).date()
        else:
            sync_date = datetime.strptime(sync_date, "%Y-%m-%d").date()

        url = "https://events.k3scluster.tech/api/events/"
        if not options["all"]:
            url += f"?changed_at={sync_date}"

        self.fetch_url(url)
        self.stdout.write(self.style.SUCCESS("Мероприятия синхронизированы"))

    def fetch_url(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR("В ходе выполнения запроса произошла ошибка")
            )
            return None
        next_page = response.json().get("next")
        results = response.json().get("results")
        self.load_events(results)
        if next_page:
            self.fetch_url(next_page)

    def load_events(self, results):
        new_events_counter = 0
        updated_events_counter = 0

        for _event in results:
            # Обработка мероприятия
            event, created = VenueEvent.objects.update_or_create(
                id=_event["id"],
                title=_event["name"],
                date=datetime.fromisoformat(_event["event_time"]),
                status=_event["status"],
            )
            if created:
                new_events_counter += 1
            else:
                updated_events_counter += 1

        # Логирование результатов синхронизации
        SyncResult.objects.create(
            sync_date=timezone.now(),
            new_events_counter=new_events_counter,
            updated_events_counter=updated_events_counter,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Синхронизация завершена: {new_events_counter} новых событий, {updated_events_counter} обновленных событий."
            )
        )
