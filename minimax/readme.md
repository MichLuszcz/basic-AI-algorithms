The program does not use any libraries besides the standard ones.

To run the application and play tic-tac-toe with a bot or observe the game between two bots, you need to execute the command:
```shell
python ./main.py [-p] [--auto]
```
-p: specifies which player is human, 1 or 2, default is 1
--auto: a flag indicating whether the game should be between two bots. If added, then yes, default is no

Usage examples:
```shell
python ./main.py 
```
runs a classic game with a bot with us as the first player

```shell
python ./main.py -p 2
```
runs a game with a bot with us as the second player
```shell
python ./main.py --auto
```
the program will conduct and show a game between two bots
Using the --auto flag ignores the -p argument.




