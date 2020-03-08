from django.test import TestCase

from beers_api.beer_reviews.test.factories.fake_review_factory import ReviewFactory
from beers_api.layered.services.reviews import ReviewService


class ReviewsServiceTest(TestCase):
    def setUp(self) -> None:
        self.review_service = ReviewService()
        self.review = ReviewFactory.build()
        self.beer_dict = {
            "name": self.review.beer_id.name,
            "type": self.review.beer_id.type,
            "alcohol": self.review.beer_id.alcohol,
        }
        self.review.beer_id.save()
        self.review_dict = {
            "beer": self.review.beer_id.id,
            "author": self.review.author,
            "rating": self.review.rating,
            "review": self.review.review,
        }

    def test_create_review(self):
        self.assertTrue(self.review_service.create_review(self.review_dict))

    def test_prepare_review_dict(self):
        review, beer = self.review_service._prepare_review_dict(self.review_dict)
        self.assertEqual(self.review.beer_id.id, beer)
        self.assertNotIn("beer", review)
        self.assertEqual(review["author"], self.review_dict["author"])
        self.assertEqual(review["rating"], self.review_dict["rating"])
        self.assertEqual(review["review"], self.review_dict["review"])
