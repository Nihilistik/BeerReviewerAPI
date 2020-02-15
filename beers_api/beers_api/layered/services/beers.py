from beers_api.beer_reviews.models.beers import Beer


class BeerService:

    def __init__(self):
        pass

    def add_beer(self, beer:dict):
        new_beer = Beer.create(beer)
        new_beer.save()
        return new_beer.id is not None
