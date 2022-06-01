# test naszego API
import requests

params = {
    'access_key': "4f0cb9a05ca9e4b845e7fbd8002ac32d",
    'flight_status': 'active',
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

for flight_info in api_response:
    airline = flight_info["airline"]
    flight = flight_info["flight"]
    departure = flight_info["departure"]
    arrival = flight_info["arrival"]
