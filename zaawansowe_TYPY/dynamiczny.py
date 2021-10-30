definicje = {}

while(True):
    print("1 : Dodaj definicje")
    print("2 : Znajdź definicje")
    print("3 : Usuń definicje")
    print("4 : Zakończ program")

    wybor = int(input("Co chcesz zrobić ? "))

    if(wybor==1):
        klucz = input("Podaj słowo kluczowe: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif(wybor==2):
        znajdz = input("Podaj słowo do przeszukania: ")
        if(znajdz in definicje):
            print(definicje[znajdz])
        else:
            print("Termin nie został znaleziony", znajdz)
    elif(wybor==3):
        usun = input("Co chcesz usunąć? ")
        if(usun in definicje):
            del definicje[usun]
            print("Usunięto definicję o nazwie: ", usun)
        else:
            print("Termin nie został znaleziony", usun)
    elif(wybor==4):
        print("elo byczku, do zobaczenia")
        break
    else:
        print("Coś poszło nie tak")


