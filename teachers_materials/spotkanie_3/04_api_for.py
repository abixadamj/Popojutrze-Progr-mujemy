import requests
import json


https_url = "https://fastapi.jurkiewicz.tech/"
# wykonujemy połączenie typu GET - analogicznie jak przeglądarka WWW
https_request = requests.get(https_url)
# tworzymy słownik (`dict`) z danych wczytanych na stronie
json_dict = json.loads(https_request.text)

# teraz wyświetlenie - w pętli iteracyjnej
for elem in json_dict:
    print(f"Klucz: {elem} ma wartość {json_dict[elem]}")