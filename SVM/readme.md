użycie:
```python .\main.py [-h] [-lamb LAMB] [-lr LR] [-e E]```

options:
-h, --help show this help message and exit

-lamb LAMB Lambda parameter for minimising (lambda * ||w||^2)

-lr LR Learning rate

-e E Number of epochs in training

LAMBDA_DEFAULT = 0.0125

LEARNING_RATE_DEFAULT = 0.001

EPOCHS_DEFAULT = 2000

Przykład:

```shell
python ./main.py 
```

```shell
python ./main.py  -lamb 1 -lr 0.1 -e 1000
```

Wartości domyślne, np Wielkośc zbioru uczacego i testującego można zmieniać w pliku constants.py
