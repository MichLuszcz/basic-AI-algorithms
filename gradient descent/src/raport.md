Celem projektu jest stworzenie solvera, który znajduje minimum dowolnej funkcji, jeśli ma wzory 
jej i jej gradientu i zbadanie, jak rozmiar kroku wpływa na wynik.
Zdefiniowałem "problem" do rozwiązania jako klasę zawierającą funkcję i jej gradient dla
łatwego dostępu i obsługi wyznaczania wartosci.

Wybieramy losowy punkt z jakiegoś przedziału, po czym sprawdzamy, jak 
dobór Bety (kontrolującej wielkość kroku) i epsilona (docelowa dokładność) wpływa
na znajdowanie minimów lokalnych funkcji. Za mała beta może powodować długie wykonywanie się algorytmu,
a zbyt duża oddalanie się od poprawnego wyniku zamiast zbliżanie się do niego.
Zbyt duży epsilon może powodować natomiast, że zatrzymamy się w poszukiwaniach na słabym rozwiązaniu. 
Mały, że nigdy nie osiągniemy porządanej dokładności przez niedoskonałość algorytmu co skutkuje długim czasem wykonania programu.
Przez "Krok" rozumiemy przesunięcie punktu z jednego miejsca w drugie

Testy funkcji 1 (x -> y)
Wybrano 100 losowych punktów z x w przedziale -5 do 5
- przy beta > 0.08, jeśli punkt początkowy jest w -5 lub 5, algorytm będzie oddalał się od poprawnej odpowiedzi

epsilon = 0.04:

beta = 0.079
 - stdev - 0.001203736168944576
 - average result: 0.0027463838311599514
 - avg amount of steps: 36.33
 - std dev of steps: 19.95097779938405
 

beta = 0.04:
standard deviation: 0.0007422295905392311
average result: 0.0031899345591240623
avg amount of steps: 87.32
std dev of steps: 29.854827198808355
# pogorszenie wyniku mimo większej liczby kroków

beta = 0.01:
standard deviation: 0.0007157092148273908
average result: 0.0032343095833989254
avg amount of steps: 373.36
std dev of steps: 111.47491632514003
# dokładność bardzo podobna, ale ilość kroków 4 razy większa

-----------
epsilon = 0.01
spodziewamy się większej dokładności i większej liczby kroków potrzebnej do jej osiągnięcia

beta = 0.079:
standard deviation: 0.00011957889746057935
average result: 0.0004992729400419287
avg amount of steps: 107.58
std dev of steps: 42.3351657918835

beta = 0.04:
standard deviation: 0.00011664693952331308
average result: 0.0005088238547962167
avg amount of steps: 227.14
std dev of steps: 71.3456545575301

beta = 0.01
standard deviation: 8.699653316408321e-05
average result: 0.0005875838474426559
avg amount of steps: 949.41
std dev of steps: 192.90758215405958

epsilon = 4:

beta = 0.079:
standard deviation: 0.40815682664775976
average result: 0.3786316585954858
avg amount of steps: 0.8
std dev of steps: 0.7247430753394787
# wiele początkowych punktów spełnia już dokładność, przez co średni wynik jest też w środku, a ilość kroków jest mniejsza niż 1

[Wykres kilku przykładów 2d tutaj]



testy funkcji 2 (x, y -> z). troche mniej niż 0.5 w najniższym, 1 w min lokalnym, ok. 1.5 na "płaskim"
dla wartości od (-4, -4) do (4, 4)

epsilon = 0.0001

beta = 0.7
standard deviation: 0.4991352924027155
average result: 1.0684837744187903
avg amount of steps: 4.93
std dev of steps: 8.291720343971223

beta = 1
standard deviation: 0.4942407589781704
average result: 0.9338058401727174
avg amount of steps: 590.0 
std dev of steps: 494.31107042371036
# widocznie więcej kroków, brak poprawy średniego wyniku

beta = 7
standard deviation: 2.1646628950017326e-06
average result: 1.4999991613194399
avg amount of steps: 23.47
std dev of steps: 48.623155102494245
# beta tak duża, że punkty często trafiają na wypłaszczenie i tam grzęzną


dla zakresu (-2, -2) do (2, 2):

epsilon = 0.01

beta = 0.7
standard deviation: 0.10014127413569401
average result: 0.5066988395703068
avg amount of steps: 8.53
std dev of steps: 5.294279359780133
    
beta = 1
standard deviation: 0.13955590287244699
average result: 0.5266347533818374
avg amount of steps: 980.0
std dev of steps: 140.7052941362897
 
beta = 3
standard deviation: 0.4778553463449902
average result: 1.00411061937985
avg amount of steps: 439.79
std dev of steps: 418.11919655195516
# tu widzimy, że mimo zakresu bardzo bliskiego minimom beta jest za duża i punkt nie ląduje głównie w minimum globalnym tylko na obrzeżach i min lokalnym

Ta metoda wyznaczania minimum funkcji jest bardzo nie efektywna w wypadku takiej funkcji.
Poza centralnymi minimami na środku osi współrzędnych funkcja jest bardzo "płaska" przez co gradient ma bardzo małą wartość i punkt nie rusza się z miejsca. 