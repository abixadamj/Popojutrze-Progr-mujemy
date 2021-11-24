# definiujemy listę - kolekcję elementów, które zachowują kolejność wprowadzania
print("---[LISTA / list]-------------------------------------------------------")
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

# odwołujemy się do poszczególnych elementów
print(f"Pełna lista: {addressbook}")
print(addressbook[0])
print(addressbook[3])
print(addressbook[5])
print(addressbook[-1])  # ostatni - liczymy indeksy ujemnie

# sprawdzamy ilość elementów
print(len(addressbook))

# sprawdzamy czy element istnieje w liście
print("Duda Andrzej" in addressbook)
print("Kaczyński Jarosław" in addressbook)

# lista potrafi być modyfikowalna w miejscu (ang. 'mutable')
print(f"Przed sortowaniem: {addressbook}")
addressbook.sort()
print(f"Po sortowaniu: {addressbook}")

print("---[SŁOWNIK / dict]-------------------------------------------------------")
# definiujemy słownik - kolekcję elementów o strukturze klucz:wartość
# które nie muszą zachowywać kolejności
addressbook = {
    "Prezydent": "Doda Andrzej",
    "Żona Prezydenta": "Kornhauser-Duda Agata",
    "Marszałek Sejmu": "Witek Elżbieta",
    "Wce - Lewica": "Czarzasty Włodzimierz",
    "Wce - PiS 1": "Gosiewska Małgorzata",
    "Wce - KO": "Kidawa-Błońska Małgorzata",
    "Wce - PiS 2": "Terlecki Ryszard",
    "Wce - KO/PSL": "Zgorzelski Piotr",
}

# odwołujemy się do poszczególnych elementów
print(f"Pełny słownik: {addressbook}")
print(addressbook["Prezydent"])
print(addressbook["Marszałek Sejmu"])
print(addressbook["Wce - KO"])
# aby działało dobrze, trzeba zakomentować poniższą linię
print(addressbook[-1])  # ostatni - ERROR !!!
# Traceback (most recent call last):
#   File "02_listy_slowniki.py", line 53, in <module>
#     print(addressbook[-1])  # ostatni - ERROR !!!
# KeyError: -1


# sprawdzamy ilość elementów
print(len(addressbook))

# sprawdzamy czy element istnieje w słowniku - szukamy tak tylko wśród kluczy
print("Duda Andrzej" in addressbook)
print("Prezydent" in addressbook)

# możemy otrzymać elementy kluczy jako listę
print(addressbook.keys())

# możemy otrzymać elementy wartości jako listę
print(addressbook.values())
