# Scenariusz/instrukcja lekcji dla nauczycieli

Temat: Spotkanie 3 - requests, API, słowniki i JSON 

Autor: **Adam Jurkiewicz**

Licencja: CC BY-SA 4.0 - https://creativecommons.org/licenses/by-sa/4.0/deed.pl

#### Opis ogólny:
>W trakcie tego spotkania poznajemy pierwszy sposób wykorzystania danych z zewnętrznego API (serwisu podającego dane).
> Zapoznamy się ze słownikiem i formatem JSON.
---

## Podstawowe treści omawiane w materiale:

- PythonConsole w PyCharm
- format `JSON` a słowniki w Pythonie
- wykorzystanie pętli `for` do wyświetlania wszystkich elementów słownika
- struktury list i słowniki jako wartości słowników
- formaty plików, elementy HTML

---

## Przebieg lekcji

### Czynności przygotowawcze przed lekcją:

1. Sprawdzamy, czy każda osoba ma działające oprogramowanie VirtualBox, dostęp do internetu. Możemy samodzielnie spróbować uruchomić kody, przeanalizować ich działanie, skonfrontować naszą wiedzę z filmami instruktażowymi.


### Faza wstępna:

1. Możemy dopytać się uczniów, czy wykonali zadania przeznaczone do pracy samodzielnej, czy mają jakiekolwiek swoje kody źródłowe.


### Faza realizacyjna:

1. #### Poznajemy `Python Console` w PyCharm + Wykorzystujemy `requirements.txt` i instalujemy niezbędne elementy: `requests`
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

2. #### Wykonujemy request z serwisu https://fastapi.jurkiewicz.tech/ i pokazujemy odczytane dane 
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.
Możemy zwrócić uwagę na złożoność obiektu zwracanego funckcją `get`:

```python
import requests
# wykonujemy połączenie typu GET - analogicznie jak przeglądarka WWW
https_request = requests.get("https://fastapi.jurkiewicz.tech/")

# wyświetlamy zawartość
print(https_request.text)

# pewien sposób stworzenia obiektu JSON
print(https_request.json())
```

3. #### `JSON` i słowniki w Python 
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.
Tu również możemy zwrócić uwagę na złożoność obiektu zwracanego funckcją `get` jak w poprzednim przykładzie.


4. #### Użycie pętli `for` dla pokazania elementów słownika z serwisu https://fastapi.jurkiewicz.tech/ 
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

5. #### Listy jako elementy słowników 
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

6. #### Słowniki jako elementy słowników
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

8. #### Edytor tekstów: eksport dokumentu do formatu PDF
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

9. #### Edytor grafiki: eksport obrazu jako PNG
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.

10. #### Edytor HTML: różne elementy na stronie (address, listy, user input, sample output)
Tu wystarczy pokazać film i postępować zgodnie ze wskazówkami.


Na koniec lekcji tworzą konta w serwisie GitHub (https://github.com/), a osoba odpowiedzialna za programowanie tworzy repozytorium projektu i udziela innym dostępu do tego repozytorium *tu się zmieni zdjęcie.*.

![](https://lh5.googleusercontent.com/xezpBszg-fHeVAYM-9-M5K7TnwgJ93iXLlntWFjZeSFD9UBIqDQgqeo3wncnTGd3dyrp1zm0AxyGH87HQxTiP-h0KfhzNMz7e8465tYYCrK_2K_znDDIxVtzejO1f9rtItlIGK-f)

### Faza podsumowująca:

1. Nauczyciel może podsumować wykonane zadanie, uczniowie mogą sprawdzić zawartość katalogu wirtualnego środowiska Python dla swojego projektu.
2. Do obejrzenia i samodzielnej pracy przeznaczone są w tym momencie następujące filmy:
   1. #### Sprawdzamy dokumentację dla przykładowych API:
    1. #### https://aviationstack.com/documentation
    2. #### https://numverify.com/documentation
    3. #### https://wttr.in/:help
2. #### Generowanie API_KEY dla wybranego projektu (Aviationstack) - https://aviationstack.com/signup/free 
3. #### Poznajemy kody odpowiedzi API: poprawnych i błędnych (3 przykłady dla każdego projektu) 
4. #### Tworzymy własne repozytorium, pamiętamy o `.gitignore`, `README.md` oraz licencji 


> UWAGA!
>
> ----
> Warto zaznaczyć, aby uczniowie dokładnie zapoznali się z tymi filmami, zwłaszcza ci, którzy są odpowiedzialni za kwestie programistyczne. W tym momencie mogą już realnie zabrać się za tworzenie aplikacji - mają **75%** informacji niezbędnych do jej wytworzenia.
> To spora dawka materiału, zwłaszcza warto zapoznać się z dokumentacjami projektu, który dana grupa chce realizować; w przykładach są tylko 3, a być może grupa wybierze zupełnie inne API.



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
