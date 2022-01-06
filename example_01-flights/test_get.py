import requests

data_get = requests.get("http://api.aviationstack.com/v1/flights?access_key=34ecfcefeab53aa9cc68ef072516d3d8&flight_status=active&offset=300")
data_json = data_get.json()
pagination = data_json["pagination"]
to_get = pagination["total"] // 100
print(f"We have total {pagination['total']} and {to_get} times 100")

for count in range(to_get+1):
    print(f"Reqest for offset = {count*100}")
    data_get = requests.get(
        f"http://api.aviationstack.com/v1/flights?access_key=34ecfcefeab53aa9cc68ef072516d3d8&flight_status=active&offset={count*100}")
    data = data_get.json()["data"]

    for flight in data:
        #  {'flight_date': '2021-10-31', 'flight_status': 'active',
        #  'departure': {'airport': 'Ben Gurion International', 'timezone': 'Asia/Jerusalem', 'iata': 'TLV', 'icao': 'LLBG', 'terminal': '3', 'gate': None, 'delay': 17, 'scheduled': '2021-10-31T09:00:00+00:00', 'estimated': '2021-10-31T09:00:00+00:00', 'actual': '2021-10-31T09:17:00+00:00', 'estimated_runway': '2021-10-31T09:17:00+00:00', 'actual_runway': '2021-10-31T09:17:00+00:00'},
        #  'arrival': {'airport': 'Charles De Gaulle', 'timezone': 'Europe/Paris', 'iata': 'CDG', 'icao': 'LFPG', 'terminal': '2A', 'gate': None, 'baggage': '08', 'delay': None, 'scheduled': '2021-10-31T13:00:00+00:00', 'estimated': '2021-10-31T13:00:00+00:00', 'actual': None,
        #  'estimated_runway': None, 'actual_runway': None},
        #  'airline': {'name': 'El Al', 'iata': 'LY', 'icao': 'ELY'},
        #  'flight': {'number': '323', 'iata': 'LY323', 'icao': 'ELY323', 'codeshared': None},
        #  'aircraft': {'registration': '4X-EDI', 'iata': 'B789', 'icao': 'B789', 'icao24': '7380C7'},
        #  'live': {'updated': '2021-10-31T08:27:57+00:00', 'latitude': 37.4, 'longitude': 28.02, 'altitude': 12184.4, 'direction': 318.78, 'speed_horizontal': 893.772, 'speed_vertical': 0, 'is_ground': False}}
        if flight["live"]:
            live = flight["live"]
            if not live["is_ground"]:
                departure = flight["departure"]["airport"]
                arrival = flight["arrival"]["airport"]
                airline = flight["airline"]["name"]
                flight_number = flight["flight"]["number"]
                aircraft = flight["aircraft"]["registration"]+" | "+flight["aircraft"]["iata"]
                pos = f"Latitude: {live['latitude']} Longitude: {live['longitude']} / Altitude: {live['altitude']}."
                print(
                    f"""Flight {flight_number} / {airline}:
From: {departure}
To: {arrival}
Aircraft: {aircraft}
Position: {pos}
---------------------------------------------------------------------------------------------"""
                )
