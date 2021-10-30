
krotka = 1,2,3,4 # krotka nie posiada nawiasów i nie można zmienić wartości krotki

# --------------------------------------SŁOWNIK-----------------------------------------

imie = str(input("Podaj imie i nazwisko: "))
number = str(input("Podaj number pokoju: "))

pokoje = {
    49:"Wojciech Chodasiewicz",
    69:"Zuzanna Trytek",
}

pokoje.update({number:imie})

print(pokoje)

# del() - do usuwnaia
# pop() - usuwa i zwraca wartość
# update() - dodaje element
# popitem() - usuwa ostatni element i go zwraca
# clear() - czyści słownik