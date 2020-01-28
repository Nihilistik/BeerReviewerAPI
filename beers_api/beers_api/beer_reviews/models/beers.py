from django.db import models
from beers_api.beer_reviews.settings import BEER_TYPES


class Beer(models.Model):
    name = models.TextField(max_length=50)
    type = models.TextField(choices=BEER_TYPES)
    alcohol = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     app_label = "Beers"
    #     db_table = "beers"

    def __str__(self):
        return f"Beer: {self.name} , {self.alcohol}º"

    def __repr__(self):
        return f"name={self.name}, type={self.type}, alcohol={str(self.alcohol)}"
