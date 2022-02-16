# Instrukcja lekcji dla nauczycieli

Temat: Lekcja 4 - funkcje, różne interfejsy API, `Commit/Push` do repozytorium

Autor: **Adam Jurkiewicz**

Licencja: CC BY-SA 4.0 - https://creativecommons.org/licenses/by-sa/4.0/deed.pl

#### Opis ogólny:
>W trakcie tego spotkania poznajemy sposoby definiowania funkcji i przestrzenie w Python (ang. `namespace`); zapoznamy się ze skryptem odczytującym i prezentującym dane z przykładowego API. W drugiej części pracujemy ze zdalnym repozytorium GitHub.
---

## Podstawowe treści omawiane w materiale:

- definiowanie funkcji
- koncepcja przestrzeni nazw w Python
- praca ze zdalnym repozytorium GitHub

---

## Przebieg lekcji

### Czynności przygotowawcze przed lekcją:

1. Sprawdzamy, czy każda osoba ma działające oprogramowanie VirtualBox, dostęp do internetu. Każdy powinien mieć konto w serwisie GitHub, pamiętać swój login i hasło. Możemy samodzielnie spróbować uruchomić kody, przeanalizować ich działanie, skonfrontować naszą wiedzę z filmami instruktażowymi.


### Faza wstępna:

1. Możemy dopytać się uczniów, czy wykonali zadania przeznaczone do pracy samodzielnej, czy mają jakiekolwiek swoje kody źródłowe.


### Faza realizacyjna:

1. #### Definiowanie funkcji w Python. 

   Funkcja - to zdefiniowany blok kodu, który realizuje pewne zadania, może bazować na różnych danych wejściowych, zwanych parametrami. Funkcja może „zwrócić” nam pewne wartości.

   Ogólny sposób definiowania funkcji w Pythonie wygląda tak:

   ```python
   def nazwa_funkcji(parametr_1, parametr_2):
       # blok kodu
       return zwracany_obiekt
   ```

   

   Zwróćmy uwagę na pewne ważne elementy:

   * słowo kluczowe `def` (*ang. define*) - mówi nam, że to będzie definicja funkcji
   * nazwa naszej funkcji zapisana jest małymi literami, jeśli zawiera dwa lub więcej słów oddzielamy je znakiem podkreślenia (to zasady z dokumentu PEP 8)
   * parametry umieszczone są w nawiasie i rozdzielone przecinkami; wywołując funkcję musimy umieścić tyle samo argumentów, co parametrów w definicji (**Uwaga!** To nie jest do końca prawda, ale na tą chwilę przejmiemy takie założenie, później, przy tłumaczeniu konkretnego kodu, poznamy więcej możliwości.)
   * znak dwukropka oznacza, że następnie występuje blok kodu i muszą być zachowane wcięcia, zgodnie z PEP 8 (4 spacje)
   * słowo kluczowe `return`  (*pol. zwróć/oddaj*) - mówi nam, że to koniec działania funkcji i zwraca `zwracany_obiekt`

   


2. #### Funkcje i zasięg zmiennych w Python. 

   W języku Python (a także w innych) istnieje pojęcie „przestrzeni nazw” - w ich obrębie każda nazwa obiektu musi być niepowtarzalna. Przestrzeń nazw najczęściej związana jest z funkcją, modułem lub plikiem, a także z obiektem. 

   Przykładowy kod pokazuje przestrzenie nazw i widoczność zmiennych w pliku `02_namespace.py`; zwróćmy uwagę na kod - widzimy w nim, jak zmienne tworzone wewnątrz definicji funkcji ***przesłaniają*** sobą tak samo nazywające się zmienne, lecz zdefiniowane w innej przestrzeni nazw.

   ```python
   # Funkcje i zasięg zmiennych w Python
   # https://tinyurl.com/popo-namespace
   # główna przestrzeń nazw: "__main__"
   # przestrzenie nazw funkcji są osobne
   some_value = 12
   some_list = [1, 2]
   
   def function_2():
       some_value = "Other value"  # zmienna rodzaju immutable
       some_list = "Other list"  # zmienna rodzaju immutable, bo przypisanie innej wartości
       print(some_value)
       print(some_list)
   
   def function_4():
       some_list.append(3)  # zmienna rodzaju mutable, do listy dodajemy element
       print(some_value)
       print(some_list)
   ```

   

3. #### Testujemy dostęp do danych API (3 przykłady dla każdego projektu) 
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami. Jednak zależy zwrócić uwagę na zmienną `api_key`, która zawiera przykładowy klucz dostępu - na 99,999% będzie on nieaktywny w momencie testowania, więc uzniowie muszą użyć swoich kluczy, które generują samodzielnie w pracy własnej.

4. #### Replikacja projektu z GitHub do PyCharm (open via VCS) i dodanie lokalnego venv (Add interpreter) i w   requirements.txt `Install all packages` a38
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

5. Dodanie do repozytorium pracy z aplikacją PySimpleGUI i `Commit/Push` a40
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

Na koniec lekcji tworzą konta w serwisie GitHub (https://github.com/), a osoba odpowiedzialna za programowanie tworzy repozytorium projektu i udziela innym dostępu do tego repozytorium *tu się zmieni zdjęcie.*.

![](https://lh5.googleusercontent.com/xezpBszg-fHeVAYM-9-M5K7TnwgJ93iXLlntWFjZeSFD9UBIqDQgqeo3wncnTGd3dyrp1zm0AxyGH87HQxTiP-h0KfhzNMz7e8465tYYCrK_2K_znDDIxVtzejO1f9rtItlIGK-f)

### Faza podsumowująca:

1. Nauczyciel może podsumować wykonane zadanie, uczniowie mogą sprawdzić zawartość katalogu wirtualnego środowiska Python dla swojego projektu.

2. Należy dokładnie zaznaczyć sposób definiowania funkcji w Python - to ważny element.

2. Do obejrzenia i samodzielnej pracy przeznaczone są w tym momencie następujące filmy:
   1. #### Sprawdzenie działania — skrypt odczytujący i prezentujący wybrane dane
   
   2. #### Wysłanie projektu do serwisu GitHub
   
   3. #### Przygotowanie dokumentacji i strony w HTML
   


> ----
>Warto zaznaczyć, że to przedostatnia dawka teorii - w tym momencie już powinni mieć zręby aplikacji gotowe.

----

## Kształtowane kompetencje kluczowe:

- kompetencje obywatelskie,

- kompetencje cyfrowe,

- kompetencje osobiste, społeczne i w zakresie umiejętności uczenia się,

- kompetencje matematyczne oraz kompetencje w zakresie nauk przyrodniczych, technologii i inżynierii.

## Cele operacyjne (językiem ucznia):

- poznasz PythonConsole w PyCharm
- poznasz format `JSON` oraz słowniki w Pythonie
- wykorzystasz pętlę `for` do wyświetlania wszystkich elementów słownika
- zaznajomisz się ze strukturą list i słowników jako wartości słowników
- zobaczysz formaty plików, elementy HTML


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

- Swoją pracę mogą wysłać do serwisu GitHub - należy ich zachęcić do tego, aby po obejrzeniu samodzielnie filmu spróbowali swoje skrypty tam wysłać.
- Jako ćwiczenie wykorzystujące nowe elementy proponuję: napisz program, który wyświetli różne informacje z API.

Przykład w pliku `99_excersises.py`:

```python
import requests


https_request = requests.get("https://fastapi.jurkiewicz.tech/")
api_data = https_request.json()
# teraz wyciągamy konkretny element z naszego słownika
header = "Client's headers"
print(f"IP klienta to {api_data[header]['x-forwarded-for']}")
print(f"Przeglądarka klienta to {api_data[header]['user-agent']}")
```
