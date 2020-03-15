import logging

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from beers_api.beer_reviews.models.beers import Beer
from beers_api.layered.api.rest.v1_0.serializers.beers import BeersSerializer
from beers_api.layered.services.beers import BeerService

logger = logging.getLogger("api_backend")
beers_service = BeerService()


class AddBeersAPIController(GenericAPIView):
    serializer_class = BeersSerializer

    def post(self, request, *args, **kwargs):
        logger.info(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        beers_service.add_beer(serializer.validated_data)
        return Response({"response": "POST ACK"})


class ListBeersAPIController(GenericAPIView):
    serializer_class = BeersSerializer

    def get(self, request, *args, **kwargs):
        beers = [beer.__dict__() for beer in Beer.objects.all()]
        serializer_beers = self.get_serializer(data=beers, many=True)
        serializer_beers.is_valid(raise_exception=True)
        return Response({"response": "GET ACK", "data": serializer_beers.data})


class ViewBeerDetailAPIController(GenericAPIView):
    serializer_class = BeersSerializer

    def get(self, request, *args, **kwargs):
        beer = beers_service.find_beer_by_id(kwargs.get("beer_id"))
        serialized_beer = self.get_serializer(data=beer.__dict__())
        serialized_beer.is_valid(raise_exception=True)

        return Response(
            {
                "response": f"GET ACK {kwargs.get('beer_id')}",
                "data": serialized_beer.data,
            }
        )
