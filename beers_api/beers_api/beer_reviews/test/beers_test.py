from django.test import TestCase
from beers_api.beer_reviews.models.beers import Beer
from .factories.fake_beer_factory import BeerFactory

class BeersModelTest(TestCase):

    def setUp(self):
        self.beer = BeerFactory.create()
        self.str_fixture = f"Beer: {self.beer.name} , {self.beer.alcohol}º"
        self.repr_fixture = f"name={self.beer.name}, type={self.beer.type}, alcohol={str(self.beer.alcohol)}"

    def test_there_are_beers(self):
        beers = Beer.objects.all()
        self.assertEqual(beers.count(), 1)

    def test_beer_str(self):
        self.assertEqual(self.str_fixture, str(self.beer))

    def test_beer_repr(self):
        self.assertEqual(self.repr_fixture, repr(self.beer))