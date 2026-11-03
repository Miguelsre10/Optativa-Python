coords = (1,3),(-2,4),(5,-7),(4,1),(5,4)
cont = 0
for c in coords:
    if c[0] > 0 and c[1] > 0:
        print(c)
        cont = cont + 1

print("Hay", cont, "coordenadas validas")