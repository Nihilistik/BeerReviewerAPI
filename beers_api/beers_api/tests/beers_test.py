import pytest
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from beers_api.beer_reviews.models.beers import Beer
from .factories.fake_beer_factory import (
    BeerFactory,
)


class BeersModelTest(TestCase):

    def setUp(self):
        self.beer = BeerFactory.create()

    def test_there_are_beers(self):
        beers = Beer.objects.all()
        self.assertEqual(beers.count(), 1)
