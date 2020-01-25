import factory
from faker import Faker
from beers_api.beers_api.beer_reviews.models.beers import (
    Beers,
    PALE,
    ALE,
    IPA,
    RED,
    BLACK
)


class BeerFactory(factory.django.DjangoModelFactory):

    faker = Faker()

    name = faker.name()
    type = faker.words(1, [
        PALE, ALE, IPA, RED, BLACK
    ], True)
    alcohol = faker.random_int()

    class Meta:
        model = Beers
