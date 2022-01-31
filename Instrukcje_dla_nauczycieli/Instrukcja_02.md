# Scenariusz/instrukcja lekcji dla nauczycieli

Temat: Spotkanie 2 - podstawowe typy danych i konstrukcje programistyczne w Python

Autor: **Adam Jurkiewicz**

Licencja: CC BY-SA 4.0 - https://creativecommons.org/licenses/by-sa/4.0/deed.pl

#### Opis ogólny:

> W trakcie tego spotkania uczniowie poznają podstawowe typy danych , konstrukcje pętli oraz instrukcji warunkowych.
> Dla aplikacji ogólnych wprowadzamy listy, warstwy i kontenery. Te elementy są ściśle powiązane z podstawą programową.
---

## Podstawowe treści omawiane w materiale:

- podstawowe typy danych w Python
- kolekcje: listy i słowniki
- importowanie funkcji z zewnętrznych modułów
- pętla iteracyjna `for...in...` oraz instrukcja warunkowa `if...elce...`
- losty w edytorze tekstów
- wastwy w edytorze graficznym
- kontenery w edytorze HTML

---

## Przebieg lekcji

### Czynności przygotowawcze przed lekcją:

1. Sprawdzamy, czy każda osoba ma działające oprogramowanie VirtualBox, dostęp do internetu. Możemy samodzielnie
   spróbować uruchomić kody, przeanalizować ich działanie, skonfrontować naszą wiedzę z filmami instruktażowymi.

### Faza wstępna:

1. Możemy dopytać się uczniów, czy wykonali zadania przeznaczone do pracy samodzielnej, czy udało im się uruchomić
   VirtualBox i zaimportować maszynę `OVA`

### Faza realizacyjna:

1. #### Podstawowe typy danych w Python, zmienne

W języku Python istnieją zmienne - nie jest to bardzo odkrywcze stwierdzenie. Zmienne zawierają wartości różnego typu, i
to na podstawie analizy tych wartości interpreter Pythona określa typ zmiennej. Nie deklarujemy typu zmiennej, musimy
pamiętać, że typ zmiennej zmienia się z jej zawartością. Musimy również pamiętać, że w języku Python rozróżniamy
wielkość liter: zmienna `linux` to coś innego niż `Linux`, a funkcja `Print()` to nie jest `print()`. To dosyć prosty
materiał - wystarczy pokazać film i postępować zgodnie ze wskazówkami. Jednak uwaga! Pośrodku filmu ujawnia się błąd! To
jest specjalne - aby pokazać, w jaki sposób Python komunikuje problemy i błędy w kodzie. W serwisie GitHub pozostawiam
kod z błędem, który uczniowie muszą samodzielnie poprawić. Wprowadzam tam od razu konwencję F-String, która jest
obecnie (rok 2021/2022) najpopularniejsza w Pythonie.

Przykład krótkiego wywołania F-String (pamiętamy o literze `f` przed znakami cudzysłowów):

```python
some_value = 3.1415

some_text = f"PI Value is: {some_value}"
print(some_text)

# inny sposób:
print(f"PI Value is: {some_value}")
```

2. #### Typy zaawansowane: listy, słowniki

W języku Python spotkamy się niejednokrotnie z *sekwencjami* - to obiekty, które składają się z wielu innych obiektów
dowolnego typu. Na początku to może być bardzo skomplikowane zdanie. W praktyce - najczęściej mówimy o prostych
sytuacjach. Tu opisane są struktury danych, które mogą przechowywać obiekty różnych typów danych.

* `<class 'list'>` Struktura **listy** (uporządkowanej kolekcji danych, zachowujących kolejność wprowadzania);
  np. `[3, 4, 5, 5, 6, 2, 4, 1]` - tutaj przykładowa lista zawierająca oceny uczennicy Beata
* `<class 'dict'>` Struktura **słownika** (nieuporządkowanej kolekcji elementów składających się z klucza i wartości);
  np. `{1: "Adam", 2: "Jurkiewicz", 3: "Linux"}` - tutaj przykładowy słownik z różnymi kluczami i wartościami Tak
  naprawdę od wersji 3.6 Pythona słowniki zachowują pewne uporządkowanie, lecz traktujmy je jako nieuporządkowane, a
  więc niezachowujące kolejności występowania elementów.

3. #### Importowanie z zewnętrznych modułów

Musimy teraz powiedzieć sobie o tych różnych możliwościach importu oraz o konsekwencjach. Oczywiście nie podamy tu
wszystkich, tylko te, które będą nam niezbędne:

* `import modul`- w ten sposób wczytujemy cały moduł, a do jego poszczególnych elementów odwołujemy się poprzez
  zapis: `modul.funkcja()`
* `from modul import *`- w ten sposób wczytujemy wszystkie elementy z modułu, a odwołujemy się poprzez zapis `funkcja()`
  , bez podawania jawnie nazwy modułu
* `from modul import funkcja_a` - w ten sposób wczytujemy tylko pewną konkretną funkcję, a odwołujemy się poprzez
  zapis `funkcja_a()`, bez podawania jawnie nazwy modułu
* `from modul import funkcja_a as funkcja_b` - w ten sposób wczytujemy tylko pewną konkretną funkcję i nadajemy jej
  własną nazwę, a odwołujemy się poprzez zapis `funkcja_b()`, bez podawania jawnie nazwy modułu

Pierwszy sposób jest najogólniejszy - stosujemy go wtedy, kiedy mamy pewność, że chcemy odwołać się do pewnych
szczególnych elementów (jak np. `sys.path`).

Drugi sposób pozwala nam w łatwy sposób mieć szybki dostęp (nie musimy dużo pisać) do wszystkich funkcji w danym module.
To dobry sposób, jeśli nie korzystamy z wielu modułów ani nie mają one dużo kodu.

Trzeci sposób jest lepszy od drugiego, gdyż wczytujemy tylko te funkcje, które potrzebujemy w naszym programie. Dzięki
temu unikniemy wczytania dwóch różnych funkcji o tej samej nazwie.

Czwarty sposób stosujemy, kiedy nazwa funkcji jest długa i chcemy sobie zaoszczędzić czasu pisania lub trafiamy na dwie
różne funkcje z dwóch modułów, lecz o tej samej nazwie.

> *Najczęściej stosujemy zapis trzeci - `from modul import funkcja_a`.*

Tu warto zauważyć, że na filmie jest już utworzony plik i kawałek kodu skopiowany z serwisu GitHub. Zrobiłem to, aby
zaoszczędzić czasu w filmie na tłumaczenie, gdyż jest to dosyć trudny temat - proponuję to przećwiczyć przed
przystąpieniem do zajęć, a uczniowie niech samodzielnie w domu też to przećwiczą, poza ćwiczeniami w szkole.

4. #### Pętla `for` i listy

Pozwala ona wykonywać blok kodu określoną liczbę razy. Python udostępnia dodatkowo dwie instrukcje, które odpowiadają za
kontrolę działania bloku kodu wewnątrz pętli:

- `break` – kończy działanie pętli, a Python przechodzi do dalszej części instrukcji – następujących po bloku pętli
- `continue` – kończy iterację bieżącej pętli, a Python wraca do początku pętli, wyrażenie warunkowe jest ponownie
  sprawdzane, aby określić, czy pętla zostanie wykonana ponownie, czy zakończyć i przejść dalej

- Tutaj na filmach w PyCharm są utworzone 2 pliki, podczas gdy w GitHub jest to jeden plik. To dla przejrzystości
  filmów. W szkole można wykonać to dowolnie - albo dwa pliki jak na filmie, albo jeden duży jak w GitHub. Pozostawiam
  to decyzji nauczycila.

5. #### Instrukcja warunkowa `if ... else ...`

Badamy w nich warunek, w zależności od wyniku tego badania wykonujemy pewien blok kodu, lub wykonujemy inny, a być może
nie wykonujemy żadnego. Bardzo uważnie musimy dobierać warunki logiczne. Możemy sprawdzić, czy wartość obiektu jest
mniejsza, większa, równa pewnej stałej wartości. Możemy sprawdzić, czy dwa obiekty na ekranie są w pewnej odległości od
siebie. W języku Python używamy następującej składni (zapisu):

```python
if warunek_1:
    # blok kodu gdy warunek_1 jest prawdą
elif warunek_2:
    # blok kodu gdy warunek_2 jest prawdą
elif warunek_3:
    # blok kodu gdy warunek_3 jest prawdą
elif warunek_n:
    # blok kodu gdy warunek_n jest prawdą
else:
    # blok kodu wykonywany wówczas, kiedy żaden z powyższych warunków nie jest spełniony
```

Minimalnie musimy podać jeden warunek, a ich maksymalna ilość jest nieograniczona. Warunki są sprawdzane w kolejności, w
jakiej je zapisujemy. W momencie, kiedy Python „napotka” warunek, który jest prawdziwy, przerywa sprawdzanie Tu
pokazujemy film i postępujemy zgodnie ze wskazówkami zawartymi na filmie..

6. #### Edytor teskstów: listy numerowane i nienumerowane

Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

7. #### Edytor grafiki: warstwy i dodanie elementu

Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

8. #### Edytor HTML: containers

Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

### Faza podsumowująca:

1. Nauczyciel może podsumować wykonane zadania,
2. Do obejrzenia i samodzielnej pracy przeznaczone są w tym momencie następujące filmy:
   1. #### Wyświetlamy informację - 1 (text)
   2. #### Rozpakowywanie tupli - pythonizm.
   3. #### Pętla `while True` - sterowanie programem PySimpleGUI
   4. #### Dodajemy elementy przycisków - 1 (button)
   5. #### Dodajemy wyświetlanie obrazków - 1 (Image)
   6. #### Poznajemy sposoby wprowadzania danych - 1 (input)
   7. #### Poznajemy sterowanie - 1 (window.read())
   8. #### PySimpleGui - tworzymy prosty program okienkowy - 1 (layout, listy)
   9. #### Wyświetlanie większej ilości danych (output)
   10. #### Edytor teskstów: zrzut zawartości okna aplikacji i dodanie do tekstu
   11. #### Edytor grafiki: warstwy i dodanie tekstu.
   12. #### Edytor HTML: różne elementy na stronie (headings, display, obrazy, listy).

> UWAGA!
>
> ----
> Warto zaznaczyć, aby uczniowie dokładnie zapoznali się z tymi filmami, zwłaszcza ci, którzy są odpowiedzialni za kwestie programistyczne.
> To spora dawka materiału, która opisuje elementy sterujące dla aplikacji okienkowej tworzonej za pomocą biblioteki **PySimpleGUI**.


----

## Kształtowane kompetencje kluczowe:

- kompetencje obywatelskie,

- kompetencje cyfrowe,

- kompetencje osobiste, społeczne i w zakresie umiejętności uczenia się,

- kompetencje matematyczne oraz kompetencje w zakresie nauk przyrodniczych, technologii i inżynierii.

## Cele operacyjne (językiem ucznia):

- Poznasz sposoby instalacji oprogramowania w systemie operacyjnym.

- Powtórzysz wiedzę o katalogach, plikach.

## Metody i techniki nauczania:

- dyskusja,

- rozmowa nauczająca z wykorzystaniem multimedium i ćwiczeń interaktywnych,

- ćwiczenia praktyczne.

## Formy pracy:

- praca indywidualna,

- praca całego zespołu klasowego.

## Środki dydaktyczne:

- komputery z głośnikami, słuchawkami i dostępem do internetu,

- zasoby multimedialne zawarte w e‑materiale,

- tablica interaktywna/tablica, pisak/kreda,

- oprogramowanie dla języka Python 3 (lub nowszej wersji), w tym PyCharm Community Edition.

## Materiały pomocnicze:

- Oficjalna dokumentacja techniczna dla języka Python 3 (lub nowszej wersji), dostępna pod
  adresem: [3.10.2 Documentation](https://docs.python.org/).
- materiały kursu OSE: https://github.com/klubmlodegoprogramisty/python/tree/main/poziom_podstawowy
- materiały książki: https://github.com/abixadamj/helion-python/tree/main/Rozdzial_1

## Wskazówki metodyczne:

- Jako ćwiczenie można zadać napisanie programu, który bazując na roku urodzenia obliczy, w którym roku dana osoba
  będzie mieć 100 lat.

Przykład:

```python
actual_year = 2022
birth = 1974
my_name = "Adam Jurkiewicz"

print(f"Hi {my_name}, we'll try to compute year of your 100 ;-)")
age = actual_year - birth
when_100 = birth + 100
text_when = f"Dear {my_name}, you will be 100 years old at {when_100}. It will be {100 - age} years from now."
print(text_when)
```