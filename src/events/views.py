from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from src.events.models import VenueEvent
from src.events.paginators import VenueEventPaginator
from src.events.serializers import VenueEventSerializer


class VenueEventListAPIView(generics.ListAPIView):
    serializer_class = VenueEventSerializer
    queryset = VenueEvent.objects.filter(status="open").select_related("venue")
    pagination_class = VenueEventPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["title"]
    ordering_fields = ["date"]
    ordering = ["date"]
    permission_classes = [
        permissions.IsAuthenticated,
    ]
