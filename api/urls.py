from django.urls import path

from .views import FlightPriceAPI, PingAPI

urlpatterns = [
    path('flights/ping/', PingAPI.as_view(), name='ping'),
    path('flights/price/', FlightPriceAPI.as_view(), name='flight-price-api'),
]
