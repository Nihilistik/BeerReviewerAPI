from django.test import TestCase
from beers_api.beer_reviews.models.reviews import Review
from .factories.fake_review_factory import ReviewFactory

class ReviewModelTest(TestCase):

    def setUp(self):
        self.review = ReviewFactory.create()
        self.str_fixture = f"Review by: {self.review.author} for beer {str(self.review.beer_id)}"
        self.repr_fixture =  f"author={self.review.author}, rating={str(self.review.rating)}, review={self.review.review}"

    def test_there_are_beers(self):
        reviews = Review.objects.all()
        self.assertEqual(reviews.count(), 1)

    def test_beer_str(self):
        self.assertEqual(self.str_fixture, str(self.review))
        self.assertIsInstance(self.review.__str__(), str)

    def test_beer_repr(self):
        self.assertEqual(self.repr_fixture, repr(self.review))
        self.assertIsInstance(self.review.__str__(), str)
