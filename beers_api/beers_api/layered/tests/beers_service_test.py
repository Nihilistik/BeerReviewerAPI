from django.test import TestCase
from beers_api.beer_reviews.models.beers import Beer
from beers_api.beer_reviews.test.factories.fake_beer_factory import BeerFactory
from beers_api.layered.services.beers import BeerService


class BeersServiceTest(TestCase):

    def setUp(self):
        self.beer = BeerFactory.create()
        self.service = BeerService()

    def test_saved_beer(self):
        res = self.service.add_beer(self.beer)
        self.assertEqual(res, True)

