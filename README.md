# TBP
Aplikacija za temporalno mjerenje i obračun troškova rada

Upute za pokretanje aplikacije

1. Pokrenuti instalacijsku skriptu za psql koja se nalazi unutar resources direktorija.
    - psqlInstall.sh

2. Instalirati psycopg2-binary modul
    - pip install psycopg2-binary

3. Instalirati PyQt5 okruženje
    sudo apt install pyqt5-dev-tools

4. Povezati se na bazu podataka
    - sudo -u postgres psql

5. Ručno unijeti sadržaj datoteke CREATE_database.sql koja se nalazi unutar resources direktorija
    - postoje razni načini za izvršiti skriptu ali meni ni jedan nije dao rezultate!!
    - jedan od načina:
        - psql -u postgres -d postgres -f CREATE_database.sql

6. Pokrenuti aplikaciju
    - python3 app.py