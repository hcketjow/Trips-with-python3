lista = [1,2,3,4,5,6]

potegiDwujki = []
for element in lista:
    potegiDwujki.append(element**2)

liczbyParzyste = []

for element in lista:
    if(element%2==0):
        liczbyParzyste.append(element)

potegiDwujki2 = [element**2 for element in range(20)]

print(potegiDwujki)
print('\n')
print(potegiDwujki2)

liczbyParzyste2 = [element for element in lista if(element%2==0)]

print(liczbyParzyste)
print('\n')
print(liczbyParzyste2)