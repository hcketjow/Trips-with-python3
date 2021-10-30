oceny = {
    "Arek": (5,2,4,1,2,3),
    "Magda": (5,3,2,3,5,5)
}

people = [
    {"name":"Arek", "age":25},
    {"name":"Jola", "age":45},
    {"name":"Wiola", "age":23},
    {"name":"Antoni", "age":21},
]

for key in oceny:
    print(key, " oceny " ,oceny[key])

for key2 in people:
    for key4 in key2:
        print(key4, key2[key4])

print('\n')

ludzie = {
    "XYSDKLAHLDKJ": {'name:':'Franek', 'age':24, 'sex':'Male'},
    "asfsdfasdfas": {'name:':'Magda', 'age':32, 'sex':'Female'},
    "rewqerqwerre": {'name:':'Julia', 'age':41, 'sex':'Female'},
    "vzxcvxcvxvcx": {'name:':'Maciek', 'age':22, 'sex':'Male'},
}

for id,test in ludzie.items():
    for demo in test:
        print(test[demo])