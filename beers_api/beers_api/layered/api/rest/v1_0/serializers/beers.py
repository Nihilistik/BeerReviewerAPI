import logging

from rest_framework import serializers

from beers_api.beer_reviews.models.beers import Beer
from beers_api.beer_reviews.settings import BEER_TYPES

logger = logging.getLogger("beers_api")


class BeersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    type = serializers.ChoiceField(choices=BEER_TYPES)
    alcohol = serializers.FloatField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Beer
        fields = "__all__"
