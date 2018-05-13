# Piłka na kartce - drobne programy w pythonie

**Opis**

* Parę skryptów umożliwiających ściaganie partii z kurnika, parsowanie danych oraz tworzenie statystyk gracza.

* Dodatkowo Paper Soccer Replay Viewer - program do przeglądania pojedyńczej partii (wymaga biblioteki PyGame) - wersję online (napisaną w JavaScript) można zobaczyć na stronie [papersoccer.pl](http://papersoccer.pl/), np. [/partia/61203900/](http://papersoccer.pl/partia/61203900/). [Orlik treningowy](http://papersoccer.pl/orlik/) dostępny na razie tylko online (JavaScript), brak wersji w pythonie.

**Przykładowe użycie**

    # W katalogu 'labs' umieściłem archiwum partii z jednego tygodnia. 

    # Rozpakowanie plików i utworzenie statystyk graczy - plik 'users.csv' 
      zawiera informacje o nazwie gracza, liczbie meczy, wygranych, przegranych,
      łącznej sumie zdobytego rankingu oraz o średnim rankingu:

    $ ./01_unpack_and_remove.sh
    $ ./02_directory_info.sh
    $ ./03_analyze_replay.sh

    # Utworzenie statystyk dla pojedyńczego gracza, np. 'skromny18' (w katalogu
      'gracze' pojawi się podkatalog o nazwie szukanego gracza wraz z wszystkimi
      partiami, które rozegrał + osobne podkatalogi z nickami przeciwników):

    $ ./05_search_single_player.sh skromny18
    $ ./07_ls_replays.sh skromny18
    $ python 08_generate_stats.py skromny18

<img src='https://raw.github.com/slunzok/papersoccer-scripts/master/screenshots/gracz.png'/>

    # Przeglądanie pojedyńczej partii (w linii 44 ustawiamy nazwę pliku, który 
      chcemy otworzyć) + jeśli potrzeba, obrócenie boiska:

    $ python replay_viewer.py
    $ python rotate_board.py

<img src='https://raw.github.com/slunzok/papersoccer-scripts/master/screenshots/partia.png'/>

    # Ściąganie partii z kurnika + (opcjonalnie) wygenerowanie pliku zawierającego
    'dobre mecze' (tzn. gdy ranking ELO każdego z graczy jest większy niż 1700)
    - ustawiamy odpowiednie zmienne start_id i end_id:

    $ python download.py
    $ python replay_analizer.py

**Licencja**

* Kod źródłowy jest dostępny na licencji MIT.

