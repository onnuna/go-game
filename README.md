# Gra Go

Gra Go to prosta implementacja gry wieloosobowej w Pythonie, wykorzystująca bibliotekę GUI tkinter do interfejsu, 
MySQL do przechowywania danych oraz gniazdka (sockets) do komunikacji sieciowej. 
Gra umożliwia dwóm graczom rozgrywkę na planszy Go o niestandardowych rozmiarach.

## Funkcje

- Interfejs graficzny (GUI) zaimplementowany za pomocą tkinter.
- Funkcjonalność wieloosobowa przy użyciu architektury klient-serwer.
- Komunikacja sieciowa obsługiwana za pomocą gniazdek (sockets).
- Rozmiary planszy od 5x5 do niestandardowych wymiarów.
- Baza danych MySQL do przechowywania wyników gry.
- Możliwość zapisu do 100 wyników gry.
- Logika gry zaimplementowana zgodnie z zasadami gry Go.

## Wymagania

- Python 3.x
- tkinter (zawarte w bibliotece standardowej Pythona)
- Serwer MySQL
- Biblioteka `mysql-connector-python` (zainstaluj za pomocą `pip install mysql-connector-python`)

## Instalacja

1. Sklonuj repozytorium:
git clone https://github.com/onnuna/go-game.git
cd go-game

2. Zainstaluj wymagane pakiety Pythona:
pip install -r requirements.txt

3. Skonfiguruj bazę danych MySQL za pomocą dostarczonego skryptu `db_setup.sql`.

4. Zaktualizuj szczegóły połączenia z bazą danych w pliku `db_config.py` zgodnie z informacjami o Twoim serwerze MySQL.

## Użycie

1. Uruchom serwer:
server.py

2. Uruchom klienta:
client.py

3. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby grać w grę.


