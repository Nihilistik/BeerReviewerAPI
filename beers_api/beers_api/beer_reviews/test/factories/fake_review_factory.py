import factory
from faker import Faker
from beers_api.beer_reviews.models.reviews import Review
from .fake_beer_factory import BeerFactory


class ReviewFactory(factory.django.DjangoModelFactory):

    beer_id = factory.SubFactory(BeerFactory)
    author = f"{Faker().first_name()} {Faker().last_name()}"
    rating = Faker().random_int(1, 5)
    review = Faker().text()

    class Meta:
        model = Review
