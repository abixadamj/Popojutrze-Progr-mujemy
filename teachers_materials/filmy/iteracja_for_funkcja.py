# lista pobrana jako wynik funkcji
import urllib.request as ureq

address = "https://abixedukacja.eu"
https_request = ureq.urlopen(address)
headers = https_request.headers.items()
print("#" * 30)
# standardowe wywołanie pętli for
for each_header in headers:
    print(f"Header of web page {address} is: {each_header}")

print("#" * 30)
# dla zainteresowanych - wykorzystanie funkcji enumerate()
for counter, each_header in enumerate(headers):
    print(f"Header number {counter} is: {each_header}")