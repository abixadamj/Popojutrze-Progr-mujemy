# kod do wykonania po kolei w Python Console
# choć można go również wykonać jako skrypt
https_url = "https://fastapi.jurkiewicz.tech/"
import requests
https_request = requests.get(https_url)
https_request.text
import json
json_dict = json.loads(https_request.text)

# teraz wyświetlenie
for elem in json_dict:
    print(f"Klucz: {elem} ma wartość {json_dict[elem]}")

# teraz konkretny element
header = "Client's headers"
print(f"IP klienta to {json_dict[header]['x-forwarded-for']}")