def leer_metricas(fichero):
    res = {}
    try:
        with open(fichero, "r") as f:
            for numero, line in enumerate(f, 1):
                parametro = line.strip().split(',')
                if len(parametro) != 3:
                    print(f"Error de formato en la línea {numero}")
                    continue
                try:
                    valor = float(parametro[2])
                except ValueError:
                    print(f"Valor no numérico en la línea {numero}")
                    continue

                if parametro[0] in res:
                    res[parametro[0]][parametro[1]] = valor
                else:
                    res[parametro[0]] = {parametro[1]: valor}
    except OSError as error:
        print(f"Error al abrir el archivo: {error}")
    return res


def analizar_metricas(res):
    sumas = {}
    cantidades = {}
    max_acc = None
    max_acc_v = None

    for modelo, metricas in res.items():
        for metrica, valor in metricas.items():
            sumas[metrica] = sumas.get(metrica, 0) + valor
            cantidades[metrica] = cantidades.get(metrica, 0) + 1

            if metrica == "accuracy":
                if max_acc_v is None or valor > max_acc_v:
                    max_acc = modelo
                    max_acc_v = valor

    promedios = {
        metrica: suma / cantidades[metrica]
        for metrica, suma in sumas.items()
    }

    print(f"Diccionario: {res}")
    print(f"Promedios: {promedios}")
    print(f"Modelo con mayor accuracy: {max_acc}")


analizar_metricas(
    leer_metricas("./Python/UD1/UD1-Realcion-2/metricas.txt")
)
