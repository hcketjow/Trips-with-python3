names = ["Wojciech", "Arek", "Maja","Aleksander","Zuzanna"]
numers = [1,2,3,4,5,6]
celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5':24}

print('\n')

namesLength = {
    name : len(name)
    for name in names   
    if name.startswith("A")
}

multipleNumber = {
    number : number*number
    for number in numers
}

Temperature = {
    key: celcius * 1.8 + 32
    for key,celcius in celcius.items()
    if celcius > -5
    if celcius < 20
}

print(namesLength)
print(multipleNumber)
print(Temperature)