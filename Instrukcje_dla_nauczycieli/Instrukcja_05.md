# Scenariusz/instrukcja lekcji dla nauczycieli

Temat: Spotkanie - praca z kluczami i wartościami słowników

Autor: **Adam Jurkiewicz**

Licencja: CC BY-SA 4.0 - https://creativecommons.org/licenses/by-sa/4.0/deed.pl

#### Opis ogólny:
>W trakcie tego spotkania poznajemy sposoby manipulowania wartościami kluczy słowników. Ta wiedza może być bardzo przydatna.
---

## Podstawowe treści omawiane w materiale:

- aktualizowanie wartości kluczy słowników
- dodawanie nowych kluczy do słowników

---

## Przebieg lekcji

### Czynności przygotowawcze przed lekcją:

1. Sprawdzamy, czy każda osoba ma działające oprogramowanie VirtualBox, dostęp do internetu. Każdy powinien mieć konto w serwisie GitHub, pamiętać swój login i hasło. Możemy samodzielnie spróbować uruchomić kody, przeanalizować ich działanie, skonfrontować naszą wiedzę z filmami instruktażowymi.


### Faza wstępna:

1. Możemy dopytać się uczniów, czy wykonali zadania przeznaczone do pracy samodzielnej, czy mają jakiekolwiek swoje kody źródłowe zaktualizowane w repozytorium w serwisie GitHub.


### Faza realizacyjna:

1. #### Aktualizowanie wartości dla kluczy słowników. 

   Warto tu zwrócić uwagę na możliwe błędy podczas odwołania się do nieistniejącego klucza, jeśli chcemy zobaczyć wartość:

   ```python
   days = {
       0: {"min_temp": 0, "max_temp": 0, "warning": False},
       1: {"min_temp": 0, "max_temp": 0, "warning": False},
       2: {"min_temp": 0, "max_temp": 0, "warning": False},
   }
   print(days[1]["min_temp"])
   print(days[2]["max-temp"])  # tu wystąpi błąd
   # Traceback (most recent call last):
   #  File "/usr/lib/python3.8/code.py", line 90, in runcode
   #    exec(code, self.locals)
   #  File "<input>", line 7, in <module>
   # KeyError: 'max-temp'
   
   # poniżej aktualizujemy wartości już istniejących kluczy
   days[1]["min_temp"] = 5
   days[2]["max_temp"] = 15  
   ```
   
   
   


2. #### Tworzenie słowników i dodawania do nich elementów. 

   Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

### Faza podsumowująca:

1. Nauczyciel może podsumować wykonane zadanie, można czas w tej lekcji wykorzystać na sesję pytań/odpowiedzi, na wspólną weryfikację dotychczasowej pracy, wiedzy.


> ----
>Warto zaznaczyć, że to ostatnia dawka teorii - w tym momencie już powinni mieć około 80% aplikacji i dokumentacji wykonane.

----

## Kształtowane kompetencje kluczowe:

- kompetencje obywatelskie,

- kompetencje cyfrowe,

- kompetencje osobiste, społeczne i w zakresie umiejętności uczenia się,

- kompetencje matematyczne oraz kompetencje w zakresie nauk przyrodniczych, technologii i inżynierii.

## Cele operacyjne (językiem ucznia):

- poznasz metody aktualizacji danych w słownikach


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
  adresem: https://docs.python.org/.
- materiały kursu OSE: https://github.com/klubmlodegoprogramisty/python/tree/main/poziom_podstawowy
- materiały książki: https://github.com/abixadamj/helion-python/tree/main/Rozdzial_1


## Wskazówki metodyczne:

- ta lekcja jest w większości już czasem dla uczniów na ostatnie zapytania.
