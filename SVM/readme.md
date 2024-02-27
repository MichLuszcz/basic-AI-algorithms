Usage:
python .\main.py [-h] [-lamb LAMB] [-lr LR] [-e E]

Options:
-h, --help Show this help message and exit

-lamb LAMB Lambda parameter for minimising (lambda * ||w||^2)

-lr LR Learning rate

-e E Number of epochs in training

LAMBDA_DEFAULT = 0.0125

LEARNING_RATE_DEFAULT = 0.001

EPOCHS_DEFAULT = 2000

Example:

```shell
python ./main.py
```

```shell
python ./main.py  -lamb 1 -lr 0.1 -e 1000
```
Default values, such as the size of the training and testing set, can be changed in the constants.py file.
