listaGosci = [
    ("Wojciech", 18, "mężczyzna"),
    ("Zuzanna", 18, "kobieta")
]

listaGosci2 = {
    ("Maciej", 18, "mężczyzna"),
    ("Michał", 18, "mężczyzna"),
    ("Magda", 18, "kobieta")
}

listaGosci3 = {
    ("Karol", 18, "mężczyzna"),
    ("Magda", 18, "kobieta")
}

# listaGosci.append(("Ola", 24, "kobieta")) #dodanie osoby do grupy
# listaGosci[0][1] = 20 # zmiana wieku 

# print(listaGosci) #Wyświeli się 18

sumaLIST = listaGosci3 & listaGosci2

print(sumaLIST)