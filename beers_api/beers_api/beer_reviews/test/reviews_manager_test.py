from django.test import TestCase

from beers_api.beer_reviews.models.reviews import Review
from beers_api.beer_reviews.test.factories.fake_review_factory import ReviewFactory


class TestReviewsManager(TestCase):
    def setUp(self) -> None:
        self.review = ReviewFactory.build()
        self.review.beer_id.save()
        self.review.save()
        self.beer = self.review.beer_id

    def test_get_by_author(self):
        author = self.review.author
        reviews = Review.objects.get_review_by_author(author)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(author, reviews[0].author)

    def test_get_by_beer(self):
        reviews = Review.objects.get_review_by_beer(self.beer)
        self.assertEqual(reviews[0].beer_id, self.beer)
