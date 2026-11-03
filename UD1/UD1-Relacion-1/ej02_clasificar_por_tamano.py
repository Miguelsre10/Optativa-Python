menores = list(())
mayores = list(())
lista = {"1", "22", "4444", "88888888", "7777777", "1", "22", "666666", "4444", "55555", "333"}
for st in lista:
    if len(st) < 5:
        menores.append(st)
    else:
        mayores.append(st)

print("\nMayores o iguales a cinco")
for s in mayores:
    print(s)
print("\nMenores a cinco")
for s in menores:
    print(s)



