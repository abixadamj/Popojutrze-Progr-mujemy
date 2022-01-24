# Progr@muj - podział materiału

# lekcje i samodzielna praca

### Podział filmów i zadań do realizacji - wersja dla potrzeb technicznych.

---

#### Ogólne założenia:

- 7 spotkań w szkole, w tym 5 poświęconych programowaniu
- 4 samodzielne prace uczniów w domu między spotkaniami poświęconymi programowaniu w szkole
- utrzymujemy wykorzystanie API w projektach ( https://any-api.com )
- będziemy korzystać z Virtualbox i OVA z Linux Ubuntu 20.04 i PyCharm wewnątrz

#### To-do w projekcie:

- [ ] Przygotowane środowisko pracy na platformie Moodle (open source) z możliwością pracy bezpośrednio przez zainteresowane szkoły, wyeksportowania pliku do wdrożenia na własnej platformie https://moodle.abixedukacja.eu/course/view.php?id=8

- [ ] Przewodnik dla uczniów dot. zakresu merytorycznego zajęć (w tym ogólnodostępnymi źródłami poszukiwania pomysłów projekty oraz  rozwiązań problemów programistycznych) oraz wprowadzenia w kontekst pracy zespołowej (case study wraz z podaniem przykładów problemów i sposobu ich rozwiązania) *dla uczniów wprowadzenie - po co w ogóle jest taki projekt*  

- [ ] Kody źródłowe do przykładowych rozwiązań, o których mowa w instrukcji dla uczniów: https://github.com/ABIX-Edukacja/programuj-w-zespole (W tej chwili dla testowania jest repo https://github.com/abixadamj/Popojutrze-Progr-mujemy)

- [x] OVA Linux z Pycharm i git i venv

- [ ] Instrukcja dla nauczyciela - tu trzeba rozpisać:
  
  - [ ] co na lekcjach w szkole (ok. 4 stron na lekcję dla nauczyciela),
  
  - [ ] co w trakcie domowych prac uczniów
  
  - [ ] jakieś pomysły dla nauczyciela o ćwiczeniach
  
  - [ ] co ma się znaleźć w dokumentacji tworzonej przez uczniów (może 1 przykładowa)

- [ ] rozpisanie filmów (wszystkich 60 sztuk, 44 Python + 1 OVA + 15 doc/graf/html)

#### Realizujemy działania w oparciu o 3 przykładowe projekty:

1. Lokalizacje lotów samolotów: https://aviationstack.com

2. Weryfikacja firm dla numerów telefonów: https://numverify.com

3. Alert pogodowy dla 3 dniowej prognozy: https://wttr.in/

*Dla chętnych na koniec zapakowanie projektu do http://www.pyinstaller.org/*

---

#### Informacja dla szkolnego administratora sieci - w celu unifikacji i ułatwienia pracy przygotowaliśmy kompletny system operacyjny Linux Ubuntu 20.04 LTS w wersji maszyny wirtualnej `OVA` dla środowiska Virtualbox.

Przed rozpoczęciem zajęć na wszystkich komputerach należy zainstalować **Virtualbox** oraz zaimportować do niego maszynę `OVA` - poniżej lista kroków do wykonania:

- Ze strony https://www.virtualbox.org/wiki/Downloads należy pobrać i zainstalować wersję 6, dla systemu Windows może to być np.:  https://download.virtualbox.org/virtualbox/6.1.32/VirtualBox-6.1.32-149290-Win.exe i zainstalować w systemie

- Ze strony https://tinyurl.com/popo-ova pobrać plik `linux_ubuntu.ova` i zapisać na dysku (**UWAGA - plik ma ok. 7 GB !!**)

- W środowisku **Virtualbox** wykonać **Import maszyny OVA**

- Po sprawdzeniu poprawności uruchamiania systemu można usunąć plik `linux_ubuntu.ova`

### Podział materiału na lekcjach:

1. Lekcja w szkole - podział, tematy itp... wstęp
2. Lekcja w szkole 
   1. Praca samodzielna
3. Lekcja w szkole
   1. Praca samodzielna
4. Lekcja w szkole
   1. Praca samodzielna
5. Lekcja w szkole
   1. Praca samodzielna
6. Lekcja w szkole
   2. Praca samodzielna      
7. Lekcja w szkole - podsumowanie projektów, post-testy itp....

*Pamiętamy, aby po każdej lekcji w szkole lub pracy samodzielnej uczestnicy zaktualizowali swoje repozytoria poprzez `Commit/Push`*

### Podział filmów - przygotowanie do utworzenia scenariuszy

#### Lekcja w szkole (1):

1. Konfiguracja IDE PyCharm, tworzenie konta w GitHub.com
2. Przygotowujemy środowisko `venv` dla lokalnego projektu
3. Plik `requirements.txt` - zewnętrzne moduły, własne pliki `py` w projekcie 
4. Minimalny program z wykorzystaniem PySimpleGUI
5. Skąd będziemy czerpać grafiki? Pixabay i Freeicon.
6. Uruchamiamy edytor tekstów - format strony.
7. Uruchamiamy edytor grafiki - otwieramy przykładowy plik graficzny.
8. Uruchamiamy edytor HTML - podstawowa strona z szablonu.
9. Edytor HTML: Bootstrap - https://getbootstrap.com/ 

#### Praca samodzielna (1):

1. VirtualBox w Windows i jak importować maszynę `OVA` - aby pracować niezależnie od szkoły
2. PySimpleGui - dokumentacja, przykłady użycia
3. Edytor teskstów: nagłówek i stopka
4. Edytor teskstów: style i spis treści
5. Edytor grafiki: zmiana rozmiaru i zapis XCF
6. Edytor HTML:  różne znaczniki `meta` 

#### Lekcja w szkole (2):

1. Podstawowe typy danych w Python, zmienne 
2. Typy zaawansowane: listy, słowniki 
3. Importowanie z zewnętrznych modułów 
4. Pętla `for` i listy
5. Instrukcja warunkowa `if ... else ...` 
6. Edytor teskstów: listy numerowane i nienumerowane 
7. Edytor grafiki: warstwy i dodanie elementu
8. Edytor HTML: containers i columns


#### Praca samodzielna (2):

1. Wyświetlamy informację - 1 (text)
2. Rozpakowywanie tupli - pythonizm.
3. Pętla `while True` - sterowanie programem PySimpleGUI
4. Dodajemy elementy przycisków - 1 (button)
5. Dodajemy wyświetlanie obrazków - 1 (Image)
6. Poznajemy sposoby wprowadzania danych - 1 (input)
7. Poznajemy sterowanie - 1 (window.read())
8. PySimpleGui - tworzymy prosty program okienkowy - 1 (layout, listy)
9. Wyświetlanie większej ilości danych (output)
10. Edytor teskstów: zrzut zawartości okna aplikacji i dodanie do tekstu
11. Edytor grafiki: warstwy i dodanie tekstu. 
12. Edytor HTML: różne elementy na stronie (headings, display, obrazy, listy).


#### Lekcja w szkole (3):

1. Poznajemy `Python Console` w PyCharm + Wykorzystujemy `requirements.txt` i instalujemy niezbędne elementy: `requests` 
2. Wykonujemy request z serwisu https://fastapi.jurkiewicz.tech/ i pokazujemy odczytane dane
3. `JSON` i słowniki w Python - 1
4. Użycie pętli `for` dla pokazania elementów słownika z serwisu https://fastapi.jurkiewicz.tech/ - i dodatkowo pokazujemy IP klienta
5. Listy jako elementy słowników - 1
6. Słowniki jako elementy słowników - 1
7. Edytor teskstów: eksport dokumentu do formatu PDF
8. Edytor grafiki: eksport obrazu jako PNG 
9. Edytor HTML: różne elementy na stronie (address, listy, user input, sample output). 


#### Praca samodzielna (3):

1. Testujemy dostęp do danych API (3 przykłady dla każdego projektu)
2. Poznajemy kody odpowiedzi API: poprawnych i błędnych (3 przykłady dla każdego projektu)
3. tworzymy własne repozytorium, pamiętamy o `.gitignore`, `README.md` oraz licencji

#### Lekcja w szkole (4):

1. Budowanie różnych interfejsów w PySimpleGUI - listy list, przykłady.
2. Replikacja projektu z GitHub do PyCharm (open via VCS) i dodanie lokalnego venv (Add interpreter) i w requirements.txt `Install all packages`
3. Dodanie do repozytorium pracy z aplikacją PySimpleGUI i `Commit/Push`
4. Sprawdzamy dokumentację dla przykładowych API:
   1. https://aviationstack.com/documentation
   2. https://numverify.com/documentation
   3. https://wttr.in/:help
5. Przygotowanie dokumentacji i strony w HTML


#### Praca samodzielna (4):

1. Testy dostępu do serwisu API
2. Definiowanie funkcji w Python
3. Sprawdzenie działania - skrypt odczytujący i prezentujący wybrane dane
4. Wysłanie projektu do serwisu GitHub

#### Lekcja w szkole (5):

1. Generowanie API_KEY  dla wybranego projektu (Aviationstack) - https://aviationstack.com/signup/free
2. Aktualizowanie wartości dla kluczy słowników - 1
3. Tworzenie słowników i dodawania do nich elementów - 1
4. Przygotowanie dokumentacji i strony w HTML

#### Praca samodzielna (5):

1. Tworzenie pełnej aplikacji
2. Tworzenie docelowego interfejsu aplikacji
3. Przygotowanie końcowe dokumentacji i strony w HTML
