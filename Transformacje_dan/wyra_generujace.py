import sys

Number1 = [element for element in range(400) if(element%2==0)]

Number2 = (element for element in range(400) if element%2==0)

for item in Number2:
    print(item)
print(sys.getsizeof(Number2))