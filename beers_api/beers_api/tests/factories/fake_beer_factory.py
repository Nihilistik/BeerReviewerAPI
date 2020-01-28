import factory
from factory import Factory
from faker import Faker
from beers_api.beer_reviews.models.beers import Beer
from beers_api.beer_reviews.settings import (
    PALE,
    ALE,
    IPA,
    RED,
    BLACK
)


Factory.faker = Faker()


class BeerFactory(factory.django.DjangoModelFactory):

    name = factory.faker.name()
    type = factory.faker.words(1, [
        PALE, ALE, IPA, RED, BLACK
    ], True)
    alcohol = factory.faker.random_int()

    class Meta:
        model = Beer
