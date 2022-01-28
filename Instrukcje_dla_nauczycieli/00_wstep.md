# Wstęp instrukcji dla nauczycieli.

> Ten wstęp opisuje najważniejsze elementy związane z naszą propozycją prowadzenia warsztatów. Zakładamy pewien podział materiałów,
> ale każdy nauczyciel może wg własnego uznania podzielić te materiały inaczej, jeśli uzna to za stosowne w ramach swoich grup.
>

---

## Informacje techniczne.

Nasz projekt oparliśmy o programowanie w języku `Python 3.8` z wykorzystaniem dodatkowych
bibliotek (`PySimpleGUI, requests`), które są ogólnodostępne. Stworzona aplikacja będzie możliwa do uruchomienia tylko
na komputerze z zainstalowanym minimum `Python 3.6`. Dodatkowo wykorzystujemy też inne aplikacje, wszystkie na otwartych
licencjach:

- edytor tekstów Libre Office Writer (https://libreoffice.org)
- edytor grafiki GIMP (https://gimp.org)
- edytor HTML Bluefish (https://bluefish.openoffice.nl)

W systemie, który jako `OVA` przygotowaliśmy w celu prostego prowadzenia zajęć, wszelkie aplikacje są już zainstalowane
i skonfigurowane.

Całość materiałów przygotowaliśmy z myślą o standardowym podziale:

- 7 spotkań/lekcji w szkole, w tym 5 poświęconych programowaniu
- min. 5 godzin samodzielnej pracy uczniów w domu między spotkaniami poświęconymi programowaniu w szkole
- w projektach zalecamy wykorzystanie ogólnodostępnych API (https://any-api.com)
- będziemy korzystać z *Virtualbox i OVA z Linux Ubuntu 20.04*

---

#### Informacja dla szkolnego administratora sieci:

w celu unifikacji i ułatwienia pracy przygotowaliśmy kompletny system operacyjny Linux Ubuntu 20.04 LTS w wersji maszyny
wirtualnej `OVA` dla środowiska Virtualbox. Przed rozpoczęciem zajęć na wszystkich komputerach należy zainstalować **
Virtualbox** oraz zaimportować do niego maszynę `OVA` - poniżej lista kroków do wykonania:

- ze strony https://www.virtualbox.org/wiki/Downloads należy pobrać i zainstalować Virtualbox w wersji 6 odpowiedniej
  dla używanego w szkole systemu operacyjnego, przykładowo: dla systemu Windows może to
  być https://download.virtualbox.org/virtualbox/6.1.32/VirtualBox-6.1.32-149290-Win.exe i zainstalować w systemie
- ze strony https://tinyurl.com/popo-ova pobrać plik `linux_ubuntu.ova` i zapisać na dysku (**UWAGA - plik ma ok. 7
  GB !!**)
- w środowisku **Virtualbox** wykonać **Import maszyny OVA**
- po sprawdzeniu poprawności uruchamiania systemu można usunąć plik `linux_ubuntu.ova`

#### Realizujemy działania w oparciu o 3 przykładowe projekty:

1. Lokalizacje lotów samolotów: https://aviationstack.com (w filmach używam tego projektu).
2. Weryfikacja firm dla numerów telefonów: https://numverify.com
3. Alert pogodowy dla 3 dniowej prognozy: https://wttr.in/

> Oczywiście, każdy zespół może sobie wybrać dowolny inny projekt (inne API, inne funkcjonalności).
> Ważne, aby zachować układ: aplikacja, dokumentacja, strona internetowa o produkcie.
> Najsłabsi mogą skorzystać z projektu Lokalizacji lotów samolotów, ważny jest proces budowania aplikacji,
> aby młodzież nauczyła się współpracy w zespole. Najbardziej kreatywni mogą zaś dowolnie kształtować wykonywane
> przez siebie projekty - nie ograniczajmy ich, nawet, jeśli przewyższają nas wiedzą techniczną.

#### Podział materiału na lekcje i pracę w domu - nasza propozycja:

1. Lekcja w szkole - podział, tematy itp... wstęp
2. Lekcja w szkole - ustawienia wstępne środowiska
    * Praca samodzielna - maszyna wirtualna i podstawy aplikacji
3. Lekcja w szkole - podstawowe typy danych i konstrukcje programistyczne w Python
    * Praca samodzielna - obsługa głównych elementów biblioteki PySimpleGUI
4. Lekcja w szkole - requests i API - słowniki i JSON
    * Praca samodzielna - samodzielne testy dostępu do API
5. Lekcja w szkole - różne interfejsy aplikacji, `Commit/Push` do repozytorium
   * Praca samodzielna - definiowanie funkcji w Python i dalsze przygotowywanie dokumentacji
6. Lekcja w szkole - praca z kluczami i wartościami słowników
   * Praca samodzielna - końcowe tworzenie dokumentacji
7. Lekcja w szkole - podsumowanie projektów, wybór najlepszego projektu, post-testy itp.

*Pamiętamy, aby po każdej lekcji w szkole (od lekcji 4) lub pracy samodzielnej uczestnicy zaktualizowali swoje
repozytoria poprzez `Commit/Push`*

---
