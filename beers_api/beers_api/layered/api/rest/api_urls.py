from django.conf.urls import include, url

urlpatterns = [
    url(r"^rest/v1_0/", include("beers_api.layered.api.rest.v1_0.api")),
]
