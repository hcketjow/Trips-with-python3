a = {1,2,3,32,-35,5} # nie wiemy jaka będzie kolejność i nie możemy zmienić elementu, nie można indexować
# a.add(7) #dodanie elementu do zbioru
b = {5,2,5123, 3421}

print(a&b) 
# set() - usuwanie duplikatów
# & - sprawdzanie wspólnych elemetnów
# - - odejmowanie zbiorów
# ^ - alternatywa wykluczająca
# | - suma elementów
# a.discard() - usuwanie elementów
# issubset() - jeden podzbiór jest podzbiorem drugiego