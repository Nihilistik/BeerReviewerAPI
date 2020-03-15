from django.urls import include, path

from beers_api.layered.api.rest.v1_0.controllers.beers import (
    AddBeersAPIController,
    ListBeersAPIController,
    ViewBeerDetailAPIController,
)

urlpatterns = [
    path("adding/beers", AddBeersAPIController.as_view(), name="adding_beers"),
    path("list/beers", ListBeersAPIController.as_view(), name="list_beers"),
    path(
        "get/beer/<int:beer_id>",
        ViewBeerDetailAPIController.as_view(),
        name="view_beer",
    ),
]
