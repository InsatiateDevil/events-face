from rest_framework import serializers

from src.events.models import VenueEvent


class VenueEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueEvent
        fields = "__all__"
