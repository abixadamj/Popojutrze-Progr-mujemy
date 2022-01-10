import requests
import json
https_url = "https://wttr.in/Warsaw?format=j1"
https_request = requests.get(https_url)
json_dict = json.loads(https_request.text)
for elem in json_dict:
    print(f"Klucz: {elem} ma wartość {json_dict[elem]}")