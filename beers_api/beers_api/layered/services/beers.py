from beers_api.beer_reviews.models.beers import Beer


class BeerService:

    def __init__(self):
        pass

    def add_beer(self, beer: dict):
        new_beer = Beer(**beer)
        new_beer.save()
        return new_beer.id is not None

    def find_beer_by_id(self, id: int):
        try:
            return Beer.objects.filter(id=id)[0]
        except IndexError as e:
            raise(e)
