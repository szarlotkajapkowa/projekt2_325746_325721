# projekt2_325746_325721
projekt_2_informatyka_geodezyjna_wtyczka qgis

# Wtyczka QGIS - Obliczanie Różnicy Wysokości i Pola Powierzchni

## Opis
Wtyczka QGIS umożliwiająca użytkownikowi obliczenie różnicy wysokości między dwoma punktami oraz pola powierzchni na podstawie współrzędnych zaznaczonych punktów metodą Gaussa.

## Funkcjonalności
- **Obliczanie różnicy wysokości:**
  - Wybór dwóch punktów z aktywnej warstwy.
  - Obliczenie różnicy wysokości między wybranymi punktami.
  - Wyświetlenie wyniku w pasku informacyjnym interfejsu QGIS.

- **Obliczanie pola powierzchni:**
  - Wybór minimum trzech punktów z warstwy.
  - Obliczenie pola powierzchni figury utworzonej przez wybrane punkty metodą Gaussa.
  - Wyświetlenie wyniku w pasku informacyjnym interfejsu QGIS.

## Wymagania
- QGIS 3.x
- Python 3.x
- PyQt5

## Instalacja
1. Sklonuj repozytorium do katalogu wtyczek QGIS:
   ```bash
   git clone https://github.com/szarlotkajapkowa/projekt2_325746_325721.git
   
2. Przenieś sklonowany katalog do katalogu wtyczek QGIS. Zwykle znajduje się on w:
   C:/Users/[TwojaNazwaUżytkownika]/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/

3. Uruchom ponownie QGIS.

##Użycie
1. Uruchom QGIS i załaduj warstwę punktową.

2. Aktywuj wtyczkę poprzez menu 'Wtyczki' -> 'Zarządzaj i zainstaluj wtyczki' -> 'wtyczka_projekt2'.

3. Po aktywacji wtyczki, pojawi się nowe okno wtyczki.

##Obliczanie Różnicy Wysokości

1.Wybierz warstwę punktową z listy rozwijanej.

2.Zaznacz dokładnie dwa punkty w wybranej warstwie.

3.Kliknij przycisk oblicz różnicę wysokości.

4.Wynik różnicy wysokości w metrach zostanie wyświetlony w pasku informacyjnym QGIS.

##Obliczanie Pola Powierzchni

1. Wybierz warstwę punktową z listy rozwijanej.

2. Zaznacz co najmniej trzy punkty w wybranej warstwie.

3. Kliknij przycisk Oblicz pole.

4. Wynik pola powierzchni w metrach kwadratowych zostanie wyświetlony w pasku informacyjnym QGIS.

##Przygotowanie Warstwy Punktowej
Wtyczka została przygotowana na podstawie plików podanych przez prowadzącego, jeśli użytkownik takich nie posiada, może sam stworzyć warstwę z własnymi punktami. 
Oto instrukcja:

Krok 1: Utworzenie warstwy punktowej

1. Otwórz QGIS.

2. Utwórz nową warstwę punktową:

-Przejdź do 'Wektor' -> 'Narzędzia tworzenia' -> 'Utwórz warstwę' -> 'Nowa warstwa obiektu geopackage....'

-Wybierz lokalizację dla swojego pliku geopackage i nadaj mu nazwę.

-Dodaj nową warstwę punktową i nazwij ją, np. 'punkty'.

-Dodaj pole atrybutu 'wysokosc' typu 'Double'.(WAŻNE----> atrybut w którym użytkownik umieści wysokości punktów musi mieć dokładną nazwe 'wysokosc', inaczej program nie zadziała)

Krok 2: Dodawanie punktów do warstwy

1. Przejdź do edycji warstwy:
   
-Kliknij prawym przyciskiem myszy na warstwę 'punkty' w panelu 'Warstwy' i wybierz 'Włącz tryb edycji' (Toggle Editing Mode).

2. Dodaj punkty do warstwy:
   
-Użyj narzędzia 'Dodaj obiekt' (Add Feature) z paska narzędziowego i kliknij na mapie, aby dodać punkty.

-W oknie dialogowym dodawania atrybutów, wprowadź wartość dla pola 'wysokosc'.

3. Zapisz zmiany:
Kliknij na ikonę 'Zapisz edycje' (Save Edits) lub wyłącz tryb edycji, a następnie potwierdź zapisanie zmian.

##Autorzy
Mateusz Bownik, Maciej Frączek
