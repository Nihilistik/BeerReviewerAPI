from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from beers_api.beer_reviews.models.managers.reviews_manager import ReviewsManager


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    beer_id = models.ForeignKey("Beer", on_delete=models.CASCADE)
    author = models.TextField(max_length=100)
    rating = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5),]
    )
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ReviewsManager()

    # class Meta:
    #     app_label = "Reviews"
    #     db_table = "reviews"

    def __str__(self):
        return f"Review by: {self.author} for beer {str(self.beer_id)}"

    def __repr__(self):
        return f"author={self.author}, rating={str(self.rating)}, review={self.review}"
