numbers = (
    number 
    for number in range(100,471)
        if(number%7==0)
        if(number%5!=0)
)

for number in numbers:
    print(number)

