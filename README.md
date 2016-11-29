# DjangoApp4LastFmCrawler
Aplikacja Django mająca za zadanie wyświetlić dane zebrane za pomocą [LastFmCrawlera](www.github.com/bieganski88/LastFmCrawler). Umożliwia wyświetlanie oraz sortowanie danych. Dwa widoki: tabelaryczny oraz mapa poglądowa.

## Zawartość
Wersja DEMO dostępna online pod adresem:
__https://mapa-koncertowa-bieganski.herokuapp.com/__
![](https://github.com/bieganski88/DjangoApp4LastFmCrawler/blob/master/events/static/events/image/mapa_readme.png?raw=True)
* SPIS KONCERTÓW - zestawienie tabelaryczne prezentujące załadowane dane, zawiera informacje o:
wykonawcy, dacie, miejscu, mieście oraz kraju gdzie odbywa się wydarzenie. Możliwość filtrowania danych dzięki wykorzystaniu pluginu jQuery DataTables.
* MAPA GŁÓWNA - podstrona prezentująca wszystkie wydarzenia muzyczne w postaci markerów na podkładzie mapowym. Jako komponent mapowy został wykorzystany Leaflet. W celu zwiększenia czytelności zastosowany został clustering - grupujący punkty zlokalizowane na tym samym obszarze. Oprócz tego panele zawierające unikatowe wartości nazw zespołów, miast, klubów oraz krajów. Wybranie, którejkolwiek z wartości powoduje przejście do widoku selekcji.
* WIDOK SELEKCJI - szczegółowy widok mapy. Zawiera wyłącznie obiekty dla okreslonej wartości zadanego kryterium. Poniżej mapy zamiast paneli tabelaryczne zestawienie zawierające pasujące obiekty
* ABOUT - podstrona zawiera informacje o autorze oraz przybliża wykorzystane technologie.

## Uruchomienie oraz podmiana danych
W celu uruchomienia aplikacji django lokalnie należy mieć zainstalowanego pythona w wersji 2.7
oraz następujące moduły:
* Django  (1.10 lub nowsze..)
* Django-Leaflet (0.9.4)

Następnie powinnismy przejść do katalogu projektowego - do folderu w którym zanjduje się
plik  ````manage.py.```` Po czym z poziomu linii komend uruchamiamy:
````
$ python manage.py runserver
````
Aplikacja powinna być dostępna pod podanym w logach adressem ip.
Domyślnie http://127.0.0.1:8000

Dane przechowywane są w pliku ````db.sqlite3```` w katalogu głównym aplikacji.
Załadowanie własnych danych jest możliwe wyłącznie lokalnie, w tym celu podczas używania
LastFmCrawlera podczas eksportu do Django należy wskazać folder, w którym znajduje się wspomniany plik.

## Prezentacja
Poniższy link prezentuje podstawową nawigację po stronie [__od 10 minuty__].
[![Everything Is AWESOME](http://img.youtube.com/vi/sULTZYII62o/0.jpg)](https://www.youtube.com/watch?v=sULTZYII62o "Link do materiału video na youtube")