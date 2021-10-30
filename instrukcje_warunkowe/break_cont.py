# wynik = 0
# i=0
# while i < 3:
#     x = int(input("Podaj liczbe: "))
#     if(x > 0 and x%2==0):
#         wynik+=x
#     else:
#         print("Liczba nie jest podzielna przez 2 lub nie jest dodatnia")
#         continue;
#     i+=1
# print(wynik)

# --------------------------------------------ZADANIE-------------------------------------------------------------

szukanaLiczba = 40
zgadnij = 0

while zgadnij != szukanaLiczba:
    zgadnij = int(input("Odgadnij liczbe: "))

    if(zgadnij > szukanaLiczba):
        print("za duża liczba ")
    elif(zgadnij < szukanaLiczba):
        print("za mała liczba ")
    else:
        print("WOW koozak z Ciebie")