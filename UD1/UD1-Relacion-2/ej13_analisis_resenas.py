with open("./Python/UD1/UD1-Relacion-2/comentarios_productos.txt", "r") as f:
    lista_pos = ["excelente","bueno", "recomendado", "satisfecho", "buen" ]
    lista_neg = ["mala", "no", "problema", "defecto"]
    n_pos=0 #numero de positivos
    n_neg=0
    n_lineas = 0
    for line in f:

        n_lineas = n_lineas + 1
        linea_pos = False
        linea_neg = False

        for palabra in line.split():
            if palabra in lista_pos:
                linea_pos = True
            if palabra in lista_neg:
                linea_neg = True

        if linea_pos:
            n_pos = n_pos + 1
        if linea_neg:
            n_neg = n_neg + 1

    #porcentaje de positivos
    p_pos = n_pos / n_lineas
    p_neg = n_neg / n_lineas

    pos = f"El % de lineas positivas es {p_pos*100}%"
    neg = f"El % de lineas negativas es {p_neg*100}%"

    print(pos)
    print(neg)

    with open("./Python/UD1/UD1-Realcion-2/resumen_sentimientos.txt", "w") as r:
        r.write(pos+"\n")
        r.write(neg)
