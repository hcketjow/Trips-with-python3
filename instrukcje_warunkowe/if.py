# a = int(input("Podaj liczbe: "))
# if(a < 5):
#     print("liczba jest mniejsza od 5")
# elif(a == 5):
#     print("liczba jest równa 5")
# else: 
#     print("liczba większa od 5")
###############################  OPERATORY LOGICZNE #############################
            # and - 'i'
            # or - 'lub'
            # not - 'zaprzeczenie' np:
                # if(not(a==5 or b==3)):
#################################################################################

wybor = input("1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie : ")
a = int(input("a = "))
b = int(input("b = "))

if(wybor == '1'):
    print(a + b)
elif(wybor == '2'):
    print(a - b)
elif(wybor == '3'):
    print(a * b)
elif(wybor == '4'):
    if(b == 0):
        print("Chyba Cię pojebało!")
    else:
        print(a / b)
else:
    print("nie wybrałeś dobrego wyboru")