from django.db import models
from django.db.models import QuerySet

from beers_api.beer_reviews.models.beers import Beer


class ReviewsManager(models.Manager):
    def get_review_by_author(self, author: str) -> QuerySet:
        return self.model.objects.filter(author=author)

    def get_review_by_beer(self, beer: Beer):
        return self.model.objects.filter(beer_id=beer)
