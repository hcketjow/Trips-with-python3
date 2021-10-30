imiona = ["Wojciech","Zuzanna","Michaś","Magda"]
liczby = [1,2,-3,4]
mieszana = ["dupa",1,"mleko",-9]

for imie in imiona:
    print(imie)

print('-----------------------------------WYPISANIE TABLICY NA 2 POZYCJI---------------------------------------------')

print(imiona[2]) 


print('------------------------------------------RÓŻNE FUNKCJE-------------------------------------------------------')

# # len() - długość:
# print(len(liczby))

# #.append - dodać coś do listy(ale tylko jeden):
# liczby.append(4)
# print(liczby)

# #extend - rozszerzyć:
# liczby.extend([2,3,4,5])
# print(liczby)

#insert(intex, 00) - wstawić
# liczby.insert(0, "Aleksandra")
# print(liczby)

#index - indeks dango el. 
# print(liczby.index(54))

# sort(reverse=False) - sortuj rosnąco
# print(liczby.sort(reverse=False))

# max() - znajdowanie największych wartości 
#min() - znajdowanie najmniejszych wartości 

# count - ile razy coś wystąpi
# print(liczby.count(4))

# pop - usuń ostatni element
# liczby.pop()

# remove - usuń pierwsze wyststąpienie
# liczby.remove(1)
# print(liczby)

# clear - wyczyść listę

# print(liczby.clear())

# reverse - zmień kolejność

# print(liczby.reverse())


print('---------------------------------------FORMUŁA IN I NOT IN-----------------------------------------------------')
# operatory in
# not in 

imie = str(input("Podaj imie: "))
liczba = int(input("Podaj liczbe: "))

if(imie in imiona):
    print("Cześć ", imie)

if(liczba not in liczby):
    print("liczby nie ma w liśćie")
else:
    print("liczba 2 jest w liście ")


