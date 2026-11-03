def leer_metricas(fichero):
    resultados = {}
    try:
        with open(fichero, "r") as f:
            for numero, linea in enumerate(f):
                parametros = linea.strip().split(',')

                if len(parametros) != 3:
                    print(f"Error de formato en la linea {numero}")
                    # rompe el bulce, como el break
                    continue

                #comprobamos que en la tercera columna hay un valor numerico para asegurar las operacines posteriores
                try:
                    valor = float(parametros[2])
                except ValueError:
                    print(f"Valor no numerico en la linea {numero}")
                    continue

                #comprobamos si la maquina esta en la lista 
                if parametros[1] in resultados:
                    resultados[parametros[0]][parametros[1]] = valor
                    #{"machine1": {"accuracy": 0.85, "loss":0.20}}
                else:
                    #si no esta añadimos la maquina a la lista con un diccionario
                    resultados[parametros[0]] = {parametros[1] : valor}
                    # creamos el diccionario machine1 : {} con el contenido, "accuracy": 0.85 en su interior
                    #{"machine1": {"accuracy": 0.85}}

    except OSError as error:
        print(f"Error al abrir el archivo: {error}")

    return resultados


def analizar_metricas(dic_metricas):
    print()





fichero = "./Python/UD1/UD1-Relacion-2/metricas.txt"
metricas = leer_metricas(fichero)
analizar_metricas(metricas)