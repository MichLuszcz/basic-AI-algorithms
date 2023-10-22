Celem projektu jest stworzenie solvera, który znajduje minimum dowolnej funkcji, jeśli ma wzory 
jej i jej gradientu i zbadanie, jak rozmiar kroku wpływa na wynik.

Wybieramy losowy punkt z jakiegoś przedziału, po czym sprawdzamy, jak 
dobór Bety (kontrolującej wielkość kroku) i epsilona (docelowa dokładność) wpływa
na znajdowanie minimów lokalnych funkcji. Za mała beta może powodować długie wykonywanie się algorytmu,
a zbyt duża oddalanie się od poprawnego wyniku zamiast zbliżanie się do niego.
Zbyt duży epsilon może powodować natomiast, że zatrzymamy się w poszukiwaniach na słabym rozwiązaniu. 
Mały, że nigdy nie osiągniemy porządanej dokładności przez niedoskonałość algorytmu.



Zdefiniowałem "problem" do rozwiązania jako klasę zawierającą funkcję i jej gradient dla
łatwego dostępu i obsługi wyznaczania wartosci.
