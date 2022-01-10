planes = [
    "Boeing 737-300",
    "Airbus A320",
    "Boeing 777-300ER",
    "Boeing 787 Dreamliner",
    "Airbus A330",
    "Boeing 747 Jumbo Jet",
    "Airbus A380",
    "Bombardier CRJ-900",
]

print(f"Pełna lista: {planes}")

print("---[Pętla iteracyjna for .. in _kolekcja_ ...]------")
# pętla iteracyjna - wykonuje się tyle razy, ile elementów posiada kolekcja
for plane in planes:
    print(f"Samolot: {plane}")
    # przykład wykorzystania wyrażenia logicznego w {}
    # zwracamy uwagę na różne znaki cudzysłowów
    print(f"Czy to jest Boeing? -> {'Boeing' in plane}")
    print(f"Czy instnieje Boeing 747 Jumbo Jet? -> {'Boeing 747 Jumbo Jet' in plane}")

print("---[Pętla warunkowa while _warunek_ ...]------")
# pętla warunkowa - wykonuje się tak długo, jak długo warunek jest prawdziwy
# w naszym wypadku element listy inny niż "Boeing 747 Jumbo Jet"
indeks = 0
while planes[indeks] != "Boeing 747 Jumbo Jet":
    print(f"Szukamy samolotu Boeing 747 Jumbo Jet, a w liście jest: {planes[indeks]} / indeks = {indeks}")
    # zwiększamy indeks
    indeks += 1
print(f"Znaleźliśmy {planes[indeks]} / indeks = {indeks}")
