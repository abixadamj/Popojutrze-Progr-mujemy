####################################################################################
# lista pobrana jako wynik funkcji i sprawdzamy czy serwer zgłasza się jako Apache
import urllib.request as ureq

address = "https://abixedukacja.eu"
https_request = ureq.urlopen(address)
headers = https_request.headers.items()
print(headers)
print("#" * 30)

server_name = headers[1]
# w tym momencie widzimy kolejny typ złożony - tuplę
# Link do dokumentacji: https://docs.python.org/3.8/library/stdtypes.html?highlight=tuple#tuple
print(f"Header is: {server_name} - type is: {type(server_name)} ")
if server_name[1] == "Apache":
    print("OK, this is Apache server")
else:
    print(f"Some strange srver type: {server_name[1]}")
print("#" * 30)
# inny sposób
if "Apache" in server_name:
    print("OK, Apache server once again...")
else:
    print("Some exception.")