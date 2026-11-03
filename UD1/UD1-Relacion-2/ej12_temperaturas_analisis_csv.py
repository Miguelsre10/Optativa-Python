with open("./Python/UD1/UD1-Relacion-2/datos.txt", "r") as f:
    next(f)
    lineas = 1
    satisfechas = 0

    for line in f:
        # eliminamos whitespaces al inicio y al final y
        # separamos los campos del csv en una lista de string
        l = line.strip().split(',')
        lineas += 1
        if int(l[2]) > 3:
            satisfechas += 1

    print(f"numero de lineas: {lineas}")
    print(f"numero de respuestas satisfechas: {satisfechas}")