# Cel zadania
Celem zadania jest stworzenie algortmu tworzącego drzewo rozgrywki w kółko i krzyżyk, potrafiącego wybierać najlepsze ruchy, odrzucając ruchy które prowadzą do przegranej. 

# Implementacja
Stworzyłem grę w kółko i krzyżyk i dwa typy graczy : człowieka, który wpisuje swoje ruchy przez konsolę, i bota, który automatycznie wybiera jeden z najlepszych możliwych ruchów poprzez sprawdzanie, do jakiej sytuacji końcowej prowadzi każdy z nich, zakładając, że przeciwnik gra optymalnie. W przypadku przegranych i remisów preferuje on, by były one jak najpóźniej w rozgrywce, bo jego przeciwnik ma wtedy szansę popełnić błąd i zmienić sytuację. W przypadku wygranych - im szybsza tym lepsza. Każda wygrana jest lepsza od remisu i każdy remis jest lepszy od przegranej. 

# Testy i symulacje
Gracz rozpoczynający gra kółkiem
### Starcia dwóch optymalnych graczy:
1: 
| O | O | X | 
__________
| X | O | O | 
__________
| O | X | X | 
__________
Draw!


2: 
| X | O | O | 
__________
| O | X | X | 
__________
| X | O | O | 
__________
Draw!


3:
| X | O | X | 
__________
| O | X | O | 
__________
| O | X | O | 
______________
Draw!


4: 

| O | X | O | 
__________
| X | X | O | 
__________
| O | O | X | 
__________
Draw!


5: 
| O | X | O | 
__________
| X | X | O | 
__________
| O | O | X | 
__________
Draw!


6: 
| O | X | O | 
__________
| O | X | O | 
__________
| X | O | X | 
__________
Draw!


7: 
| X | O | X | 
__________
| O | X | O | 
__________
| O | X | O | 
__________
Draw!


8: 
| X | O | X | 
__________
| X | O | O | 
__________
| O | X | O | 
__________
Draw!


9: 
| X | O | X | 
__________
| X | O | O | 
__________
| O | X | O | 
__________
Draw!


10: 
| X | O | O | 
__________
| O | X | X | 
__________
| X | O | O | 
__________
Draw!


Jak widać w takim starciu zawsze dochodzi do remisu. Niektóre stany końcowe powatrzają się ze względu na symetryczność i niskie skomplikowanie gry - jest dosyć mała liczba (ok 3, plus wszystkie ich odbicia względem osi x i y)  końcowych stanów remisowych do których dążą algorytmy. Oba wiedzą, że jeśli przeciwnik będzie grać optymalnie, to najlepszym końcem jest właśnie remis. 



### Starcie losowego z optymalnym (rozpoczyna losowy)

1:
| X | O | O | 
__________
| O | X | X | 
__________
|     | O | X | 
__________
Winner:minimax


2:
| O | X | O | 
__________
| O | X |     | 
__________
|     | X |     | 
__________
Winner:minimax


3:
| X | O | X | 
__________
| O | X |    | 
__________
| O | O | X | 
__________
Winner:minimax


4:
| X | X | X | 
__________
| X | O | O | 
__________
| O |    | O | 
__________
Winner:minimax


5:
|     | O |     | 
__________
| O | O |     | 
__________
| X | X | X | 
__________
Winner:minimax


6: 
| X |     |     | 
__________
| X | O | O | 
__________
| X |     | O | 
__________
Winner:minimax


7:
| X | O | X | 
__________
|     | X | O | 
__________
| O | O | X | 
__________
Winner:minimax


8:
| O | X | O | 
__________
| O | O | X | 
__________
| X | O | X | 
__________
Draw!


9:
| O | O |    | 
__________
| X | X | X | 
__________
| O |    |    | 
__________
Winner:minimax


10:
| O |    |    | 
__________
| X | X | X | 
__________
| O | O |   | 
__________
Winner:minimax
##### Wynik testów dla wielu gier losowego vs minimax:
random1 vs minimax1 win ratio in 500 games :
random: 0 (0.0%) / minimax: 398 (79.6%) / draws: 102 (20.4%). 


### Starcie minimax z losowym (minimax zaczyna) 

1:
| X |     | O | 
__________
| O | O | O | 
__________
| X |     | X | 
__________
Winner:minimax1


2:
| O |     |    | 
__________
|     | O |    | 
__________
| X | X | O | 
__________
Winner:minimax1


3:
| O | O | X | 
__________
| X | X | O | 
__________
| O | O | X | 
__________
Draw!


4:
|     | X |     | 
__________
| O | O | O | 
__________
|     | X |     | 
__________
Winner:minimax1


5:
|    |     | O | 
__________
| X |     | O | 
__________
| X |     | O | 
__________
Winner:minimax1


6:
| O | O |    | 
__________
|    | O | X | 
__________
| X | O | X | 
__________
Winner:minimax1


7:
| X | X | O | 
__________
| O | X | X | 
__________
| O | O | O | 
__________
Winner:minimax1


8:
| X |     |     | 
__________
| X |     |     | 
__________
| O | O | O | 
__________
Winner:minimax1


9:
| O | X | O | 
__________
| O | X | X | 
__________
| X | O | O | 
__________
Draw!


10:
| O | O |    | 
__________
|    | O | X | 
__________
| X | O | X | 
__________
Winner:minimax1
##### Wyink testów dla większej próby:
minimax1 vs random1 win ratio in 200 games :
minimax: 192 (96.0%) / random: 0 (0.0%) / draws: 8 (4.0%).

Jak widać kiedy to minimax zaczyna rozgrywkę, zdecydowanie rzadziej dochodzi do remisów (tylko w 4% gier), podczas gdy to losowy gracz zaczynał, było to aż 20.4% gier


### Podsumowanie wyników:
###### minimax1 vs random1 win ratio in 200 games :
minimax: 192 (96.0%) / random: 0 (0.0%) / draws: 8 (4.0%). 
![[Pasted image 20231126194804.png]]
###### random1 vs minimax1 win ratio in 500 games :
random: 0 (0.0%) / minimax: 398 (79.6%) / draws: 102 (20.4%). 
![[Pasted image 20231126195105.png]]


###### random1 vs random2 win ratio in 500 games :
p1: 300 (60.0%) / p2: 135 (27.0%) / draws: 65 (13.0%). 

![[Pasted image 20231126195425.png]]