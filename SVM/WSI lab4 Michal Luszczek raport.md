# Cel zadania
Stworzenie maszyn wektorów nośnych do rozpoznawania cyfr ze zbioru MNIST.

## Eksperymenty:

**Klasa -1 oznacza, że żaden ze składowych SVMów nie rozpoznał danego osobnika jak swoją liczbę**
#### Przetestujmy różne kombinacje danych
Przykłady:
Lambda 1
learning rate = 1
epoki = 1000

![[Pasted image 20231213180238.png|450]]
Algortym kompletnie nie rozpoznaje cyfry 5

|   | precision   | recall  | f1-score |   support |
|----------------- |   ------   |  ---------|-----------|---------|        
|0     |  1.00   |   1.00  |    1.00   |     85|
|1     |  1.00   |   1.00   |   1.00     |  126
|2     |  1.00    |  1.00   |   1.00     |  116
| 3    |   1.00    |  1.00  |    1.00    |   107|
|4    |   1.00    |  1.00   |   1.00    |   110|
|5    |   0.00   |   0.00  |    0.00    |    87|
|6   |    1.00   |   1.00  |    1.00     |   87|
|7   |    1.00    |  1.00  |    1.00      |  99|
|8   |    1.00   |   1.00  |    1.00    |    89|
|9   |    1.00   |   1.00  |    1.00     |   94|
|weighted avg|      0.91  |    0.91 |     0.91   |   1000|

accuracy   0.91




----


lambda = 0.0125
learning rate = 0.001
epoki = 2000

celność = 0.74
Confusion matrix:
![[Pasted image 20231213171359.png|450]]

		      precision  recall   f1-score   support

          -1       0.00      0.00      0.00         0
           0       1.00      0.95      0.98        85
           1       1.00      0.92      0.96       126
           2       1.00      0.78      0.88       116
           3       1.00      0.71      0.83       107
           4       1.00      0.75      0.86       110
           5       1.00      0.74      0.85        87
           6       1.00      0.85      0.92        87
           7       1.00      0.70      0.82        99
           8       1.00      0.27      0.42        89
           9       1.00      0.66      0.79        94

	accuracy                       0.74      1000
	macro avg  0.91      0.67      0.76      1000




Algortym ma problem z rozpoznawaniem cyfry 8

-----
lambda 0.009 
learning rate 0.0005 
epoki 3000
 
celność =  0.755
![[Pasted image 20231213174707.png|450]]

                precision    recall  f1-score   support

          -1       0.00      0.00      0.00         0
           0       1.00      0.95      0.98        85
           1       1.00      0.92      0.96       126
           2       1.00      0.76      0.86       116
           3       1.00      0.71      0.83       107
           4       1.00      0.76      0.87       110
           5       1.00      0.74      0.85        87
           6       1.00      0.86      0.93        87
           7       1.00      0.75      0.86        99
           8       1.00      0.36      0.53        89
           9       1.00      0.69      0.82        94

	accuracy                        0.76      1000
	macro avg   0.91      0.68      0.77      1000


Cyfry 1 i 2 rozpoznaje prawie idealnie, resztę w 3/4 przypadków, ponownie ma problem z cyfrą 8.





Zbiór testów efektywności dla 1000 epok treningowych:

| Lambda \ learning rate | 1    | 0.5   | 0.1 | 0.01 |
| ----------------------|---    | ----  | ----|  --- |
| 1                     | 0.913 | 0.397 |0.121| 0.123      |
| 0.5                   | 0.397 | 0.316 |0.094| 0.228    |
|0.1                    | 0.19  | 0.135 |0.304|  0.598    |
|0.01                   | 0.519 | 0.475 | 0.76 |0.747      |


Zastosowanie parametrów większych niż 1 skutkuje przepełnieniem (overflow) podczas mnożenia wewnątrz algorytmu.


# Wnioski
Najlepszymi parametrami okazały się lambda = 1 i learning rate = 1, pomimo tego, że zwykle przyjmuje się learning rate rzędu 0.01. Jednak przy takich parametrach SVM mający rozpoznawać cyfrę 5 nigdy jej nie rozpoznawał, mimo że przy innych parametrach już tak. Można to naprawić wstawiając odrębne parametry dla tego konkretnego SVM podczas ich tworzenia. 

Jeśli dla SVM mającego odróżniać 5 od innych cyfr przyjmiemy parametry 
lambda = 0.01
learning rate = 0.1
a dla wszystkich innych 
lambda = 1
learning rate =1
to otrzymujemy maszynę potrafiącą rozróżniać cyfry z tego zbioru z efektywnością 
0.986, czyli 98.6%.

![[Pasted image 20231213204707.png|450]]

Poza parametrami 1/1 zadowalające wyniki dają też parametry bardzo małe: lambda = 0.01, learning rate = 0.1 lub 0.01, lecz nie tak dobre jak w przypadku poprzednim.