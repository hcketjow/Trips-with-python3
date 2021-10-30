# -----------------------------------------------PĘTELKA WHILE---------------------------------------------------
# wynik = 0
# i=0
# while i < 4:
#     x = int(input("Podaj liczbe: "))
#     wynik+=x
#     i+=1

# print("Wynik dodawanie liczb to : ", wynik)

# -----------------------------------------------PĘTELKA FOR----------------------------------------------------

# wynik=0
# for i in range(4):
#     if(i%2==0):
#         print("parzysta", i)
#         # x = int(input("Podaj wartosc: "))
#         # wynik+=x
#     # print(i%2==0) #liczba parzysta
#     # print(i%2==1) #liczba nieparzysta

# print("Wynikiem dodawanie == ", wynik)

# ---------------------------------Zadanie-----------------------------------
for i in range(200):
    if(i%5==0):
        print("liczba", i," podzielna przez 5")
    elif(i%7==0):
        print("liczba", i,"podzielna przez 7")
    else:
        print("liczba", i ,"nie dzieli sie przez 7 i przez 5")