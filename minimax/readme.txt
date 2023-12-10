Program nie używa żadnych zewnętrznych bibliotek poza standardową

Aby uruchomić aplikację i zagrać w kółko i krzyżyk z botem lub obserwować rozgrywkę między dwoma botami należy
wykonać polecenie:
'python ./main.py [-p] [--auto]'
-p : ktorym graczem jest czlowiek, 1 lub 2, domyślnie 1
--auto : flaga określająca czy gra ma być między dwoma botami. Jeśli jest dodana to tak, domyślnie nie

Przykłady użycia:
`python ./main.py` uruchamia klasyczną rozgrywkę z botem z nami jako pierwszym graczem
`python ./main.py -p 2` uruchamia rozgrywkę z botem z nami jako drugim graczem
`python ./main.py --auto` program przeprowadzi i pokaże rozgrywkę dwóch botów
użycie flagi --auto powoduje zignorowanie argumentu -p