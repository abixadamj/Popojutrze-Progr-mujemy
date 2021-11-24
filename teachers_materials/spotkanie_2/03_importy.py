import urllib.request

https = "https://abixedukacja.eu"
http_request = urllib.request.urlopen(https)

headers = http_request.headers.items()
print(f"Headers of web page: {headers}")

# inny sposób importowania
from random import randint, random
from time import sleep
from turtle import *

print(f"Całkowita liczba pseudolosowa z zakresu -100 do 100: {randint(-100,100)}")
print(f"Pseudolosowa wartość z zakresu [0,1): {random()}")

# teraz grafika żółwia
pensize(20)
color("red")
forward(100)
left(90)
color("green")
forward(100)
left(90)
color("yellow")
forward(100)
left(90)
color("blue")
forward(100)

# wstrzymujemy na 10 sekund
sleep(10)
