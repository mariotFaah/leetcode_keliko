myArray = [21, 12, 34, 53, 23, 53, 2, 4]
minValue = myArray[0]

for i in myArray:
    if i < minValue:
        minValue = i

print(f"{minValue} est le valeur minimale")
