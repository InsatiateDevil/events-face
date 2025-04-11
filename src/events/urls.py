from django.urls import path

from .views import VenueEventListAPIView

urlpatterns = [
    path("events/", VenueEventListAPIView.as_view(), name="event-list"),
]
