from django.db import models
PALE = "PALE"
ALE = "ALE"
IPA = "IPA"
RED = "RED"
BLACK = "BLACK"

BEER_TYPES = [
    (PALE, PALE),
    (ALE, ALE),
    (IPA, IPA),
    (RED, RED),
    (BLACK, BLACK),
]


class Beers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    type = models.TextField(choices=BEER_TYPES)
    alcohol = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "Beers"
        db_table = "beers"
