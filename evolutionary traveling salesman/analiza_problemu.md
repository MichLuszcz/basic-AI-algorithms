Potrzebuję algorytmu który znajdzie najkrótszą drogę między punktami, odwiedzi każdy dokładnie raz i następnie wróci do początkowego
osobnik:
- numerujemy każde miasto i osobnikiem jest lista kolejno odwiedzonych miast (int[]), będąca permutacją liczb określających nr miasta, z dodanym pierwszym miastem na końcu
- podczas mutacji zamieniamy miasta miejscami, powiedzmy lecąc przez połowę listy albo całą opisującej drogę i losowanie czy dane miasto powinno być zamienione czy nie.
