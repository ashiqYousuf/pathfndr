import json

import requests
from django.conf import settings
from django.core.cache import cache

from .constants import (AMADEUS_CACHE_PREFIX, AMADEUS_FLIGHT_SEARCH_EXPIRY,
                        AMADEUS_LOGIN_EXPIRY)


class Amadeus:

    def __init__(self):
        cache_key = f"{AMADEUS_CACHE_PREFIX}:access_token"
        access_token = cache.get(cache_key)

        if access_token:
            self.access_token = access_token
        else:
            LOGIN_URL = settings.AMADEUS_LOGIN_ENDPOINT[settings.AMADEUS_API_ENV]
            response = requests.post(LOGIN_URL, data={
                "grant_type": "client_credentials",
                "client_id": settings.AMADEUS_API_KEY,
                "client_secret": settings.AMADEUS_API_SECRET
            })

            if response.status_code == 200:
                access_token = json.loads(response.text)["access_token"]
                cache.set(cache_key, access_token, AMADEUS_LOGIN_EXPIRY)
                self.access_token = access_token
            else:
                print(f"Could not log in to amadeus. {
                    response.status_code} {response.content}")

    def send(self, endpoint):
        print(f"Hitting Amadeus API: {endpoint}")
        response = requests.get(
            endpoint, headers={'Authorization': f'Bearer {self.access_token}'})

        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        print(f"Error from amadeus: {response.status_code} {response.content}")
        return None

    def get_cheapest_flight(self, org_code="", dest_code="", depart_date="", num_adults=1, num_results=1):
        """
        This method returns the cheapest flight between source and destination.
        """
        url = f'{
            settings.AMADEUS_FLIGHT_SEARCH_ENDPOINT[settings.AMADEUS_API_ENV]}'
        q_params = f'originLocationCode={org_code}&destinationLocationCode={
            dest_code}&departureDate={depart_date}&adults={num_adults}&max={num_results}'
        endpoint = f'{url}?{q_params}'
        data = self.send(endpoint)
        return data

# class Amadeus:

    # def airport_routes(self, departure_code, arrival_country, max_results=100):
    #     cache_key = f'{self.__class__.AIRPORT_ROUTES_CACHE_PREFIX}{
    #         departure_code}:{arrival_country}'
    #     data = rcache.get(cache_key)
    #     if not data:
    #         print(f"Cache miss: {cache_key}")
    #         data = self.send(self.__class__.AIRPORT_ROUTES_EP + f'?departureAirportCode={departure_code}'
    #                          f'&arrivalCountryCode={arrival_country}&max={max_results}')
    #         rcache.set(cache_key, data)
    #     else:
    #         print(f"Cache hit: {cache_key}")
    #     return data
