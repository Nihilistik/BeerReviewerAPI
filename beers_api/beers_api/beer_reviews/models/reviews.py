from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    beer_id = models.ForeignKey('Beers.Beers', on_delete=models.CASCADE)
    author = models.TextField(max_length=100)
    rating = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "Reviews"
        db_table = "reviews"
