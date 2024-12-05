# Pathfndr problem


## Assumption: I have used default sqlite database provided by django, but my codebase is flexible for extension.


## Assumption: Make sure you have docker and docker-compose installed in your system and your PORT 6379 is free for communication.


## Steps to run the project:-


    1. Make a .env file in the root of your project and copy the env variables from example.env, obtain your AMADEUS_API_KEY and 
    AMADEUS_API_SECRET from amadeus and paste them in .env file at appropriate place.


    2. Run the command: docker compose up


## Project APIs:


    1. Ping endpoint: http://127.0.0.1:8000/flights/ping/


    2. Flight Search Endpoint: http://127.0.0.1:8000/flights/price/?org_code=BLR&dest_code=SXR&num_adults=1&depart_date=2024-12-28&no_cache=0


## Access Token Management:


    1. I have managed acccess token automatically before invoking Amadeus flight search API.


    2. I have saved access token in cache for 25 minutes to make sure not to make any unnecessary api hits.

    
    3. As the access token gets expired, it gets removed from the cache automatically and we obtain a new access token before a new flight search API call is made.
