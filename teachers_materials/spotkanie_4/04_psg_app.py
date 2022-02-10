# Dodanie do repozytorium pracy z aplikacją PySimpleGUI i `Commit/Push` a37
# uwaga na ilość uruchomień: 100 request ogólnie, później:
# {'error': {'code': 'usage_limit_reached', 'message': 'Your monthly usage limit has been reached. Please upgrade your Subscription Plan.'}}
# wczytujemy niezbędne elementy
import sys
import requests
import PySimpleGUI as sg


def get_planes_in_air(desired_city, api_key):
    returned_text = f"No planes found for: {desired_city}"
    data_get = requests.get(
        f"http://api.aviationstack.com/v1/flights?access_key={api_key}&flight_status=active&offset=300")
    data_json = data_get.json()

    # sprawdzamy, czy nie pojawia się jakiś błąd
    if "error" in data_json:
        return data_json["error"]["message"]

    # jeśli błędnie podamy api_key
    if data_get.status_code == 401:
        return data_json["error"]["message"]

    pagination = data_json["pagination"]
    to_get = pagination["total"] // 100
    for count in range(to_get + 1):
        print(f"Reqest for offset = {count * 100}")
        data_get = requests.get(
            f"http://api.aviationstack.com/v1/flights?access_key={api_key}&flight_status=active&offset={count * 100}")
        data = data_get.json()["data"]
        for flight in data:
            if flight["live"]:
                live = flight["live"]
                if not live["is_ground"]:
                    departure = flight["departure"]["airport"]
                    arrival = flight["arrival"]["airport"]
                    airline = flight["airline"]["name"]
                    flight_number = flight["flight"]["number"]
                    aircraft = flight["aircraft"]["registration"] + " | " + flight["aircraft"]["iata"]
                    pos = f"Latitude: {live['latitude']} Longitude: {live['longitude']} / Altitude: {live['altitude']}."
                    if arrival == desired_city:
                        output_line = f"""Flight {flight_number} / {airline}:
From: {departure}
To: {arrival}
Aircraft: {aircraft}
Position: {pos}
---------------------------------------------------------------------------------------------"""
                        returned_text += output_line

        return returned_text


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Checking planes around")],
    [sg.Text("Please enter API KEY"), sg.Input("api_key")],
    [sg.Text("Please enter name of city of arrival"), sg.Input("City"), sg.Button("Check flights")],
    [sg.Text("_" * 100)],
    [sg.Output(size=(100, 15), key="-OUTPUT-")],
    [sg.Button("Clear -OUTPUT-"), sg.Exit()],
]
window = sg.Window("Checking planes in air around our location.", app_layout, enable_close_attempted_event=True)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    # inny sposób sprawdzania - tu x nie spowoduje zniknięcia okna
    if event in (sg.WINDOW_CLOSE_ATTEMPTED_EVENT, "Exit") and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        print("Break and EXIT")
        break

    # dodajemy sprawdzenie wciśniętego przycisku
    if event == "Check flights":
        # sprawdzamy loty
        api_key = values[0]
        desired_city = values[1]
        planes_in_air = get_planes_in_air(desired_city, api_key)
        print(planes_in_air)

    # sprawdzamy naciśnięte przyciski
    if event == "Clear -OUTPUT-":
        window['-OUTPUT-'].update(value='')

# koniec programu
window.close()
print("End of application")
sys.exit()