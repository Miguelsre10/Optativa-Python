datos = ["Ciudad,Temperatura\n","Madrid,32\n","Barcelona,30\n","Sevilla,35\n","Valencia,31\n"]

with open("./Python/UD1/UD1-Relacion-2/datos_temperatura.txt", "w") as f:
    f.writelines(datos)


with open("./Python/UD1/UD1-Relacion-2/datos_temperatura.txt", "r") as f:
    #saltamos la cabezera
    next(f)
    temps = []
    total=0

    for line in f:
        l = line.strip().split(',')
        if int(l[1]):
            print(l[1])
            temps.append(int(l[1]))


    for i in temps:
        total = total + i

    media = total / len(temps)
    print(f"La media de temperaturas es {media}")