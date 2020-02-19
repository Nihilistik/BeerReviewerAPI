import pytest
from django.test import TestCase
from beers_api.beer_reviews.models.beers import Beer
from beers_api.beer_reviews.test.factories.fake_beer_factory import BeerFactory
from beers_api.layered.services.beers import BeerService
from django.forms.models import model_to_dict


class BeersServiceTest(TestCase):

    def setUp(self):
        self.beer = BeerFactory.build()
        self.service = BeerService()

    def test_saved_beer(self):
        res = self.service.add_beer(model_to_dict(self.beer))
        self.assertEqual(res, True)


    def test_retrieved_beer(self):
        self.beer.save()
        same_beer = self.service.find_beer_by_id(self.beer.id)
        self.assertEqual(self.beer, same_beer)

    def test_no_beer_found(self):
        with pytest.raises(IndexError):
            self.service.find_beer_by_id(999)
