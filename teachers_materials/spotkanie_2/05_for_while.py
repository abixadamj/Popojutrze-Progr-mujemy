addressbook = [
    "Duda Andrzej",
    "Kornhauser-Duda Agata",
    "Witek Elżbieta",
    "Czarzasty Włodzimierz",
    "Gosiewska Małgorzata",
    "Kidawa-Błońska Małgorzata",
    "Terlecki Ryszard",
    "Zgorzelski Piotr",
]

print(f"Pełna lista: {addressbook}")

print("---[Pętla iteracyjna for .. in _kolekcja_ ...]------")
# pętla iteracyjna - wykonuje się tyle razy, ile elementów posiada kolekcja
for name in addressbook:
    print(f"Osoba: {name}")
    # przykład wykorzystania wyrażenia logicznego w {}
    # zwracamy uwagę na różne znaki cudzysłowów
    print(f"Czy o nazwisku Duda? -> {'Duda' in name}")

print("---[Pętla warunkowa while _warunek_ ...]------")
# pętla warunkowa - wykonuje się tak długo, jak długo warunek jest prawdziwy
# w naszym wypadku element listy inny niż "Terlecki Ryszard"
indeks = 0
while addressbook[indeks] != "Terlecki Ryszard":
    print(f"Szukamy Pana Terleckiego, a w liście jest: {addressbook[indeks]}")
    # zwiększamy indeks
    indeks += 1
