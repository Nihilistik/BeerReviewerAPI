from beers_api.beer_reviews.models.reviews import Review
from beers_api.layered.services.beers import BeerService


class ReviewService:
    def __init__(self):
        self.beer_service = BeerService()

    def create_review(self, review: dict) -> bool:
        prepared_review, beer_id = self._prepare_review_dict(review)
        new_review = Review(**review)
        new_review.beer_id = self._get_beer_from_review(beer_id)
        new_review.save()
        return new_review.id is not None

    def get_review_from_author(self, author: str) -> list:
        return list(Review.objects.get_review_by_author(author))

    def _prepare_review_dict(self, review: dict) -> tuple:
        beer = review["beer"]
        del review["beer"]
        return review, beer

    def _get_beer_from_review(self, beer_id: int):
        try:
            return self.beer_service.find_beer_by_id(beer_id)
        except IndexError as e:
            raise e
