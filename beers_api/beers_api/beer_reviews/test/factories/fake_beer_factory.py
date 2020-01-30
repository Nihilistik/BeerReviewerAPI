import factory
from faker import Faker
from beers_api.beer_reviews.models.beers import Beer
from beers_api.beer_reviews.settings import (
    PALE,
    ALE,
    IPA,
    RED,
    BLACK
)


class BeerFactory(factory.django.DjangoModelFactory):

    name = Faker().name()
    type = Faker().words(1, [
        PALE, ALE, IPA, RED, BLACK
    ], True)
    alcohol = Faker().random_int()

    class Meta:
        model = Beer
