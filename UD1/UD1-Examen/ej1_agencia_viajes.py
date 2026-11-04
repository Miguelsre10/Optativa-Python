# Miguel San Roman Espejo
# 04/11/2026


def anailis_exlporatorio(fichero):
    datos = {}
    listaClaves = []
    with open(fichero, "r") as f:
        for numero, linea in enumerate(f):
            parametros = linea.strip().split(',')

            #comprobamos que el numero de parametros sea correcto
            if len(parametros) != 4:
                print(f"Error de formato en la linea {numero}")
                # rompe el bulce, como el break
                continue

            # si estamos en la primera linea metemos como claves de los diccionarios los nombres de las columnas del CSV 
            if(numero == 0):
                for clave in parametros:
                    datos[clave] = []
                    listaClaves.append(clave)

            else:
                #comprobamos que en la tercera columna hay un valor numerico para asegurar las operacines posteriores
                try:
                    valor = float(parametros[2])
                except ValueError:
                    print(f"Valor no numerico en la linea {numero}")
                    continue

                #comprobamos que en la cuarta columna hay un valor numerico para asegurar las operacines posteriores
                try:
                    valor = int(parametros[3])
                except ValueError:
                    print(f"Valor no numerico en la linea {numero}")
                    continue

                for i, dato in enumerate(parametros):
                    datos[listaClaves[i]].append(parametros[i])
            
        #print(datos)
        return datos

fichero = "./Python/UD1/UD1-Examen/reservas_viajes.csv"
datos = anailis_exlporatorio(fichero)

totalRegistros = 0
precioMedio=0
diccReservas = {}
MasVendido = ""
MasVendido_unidades = 0
diccFacturacionProductos = {}

# apartado A
#no requiere conocer las claves del diccionario de datos
for campo, lista_datos in datos.items():
    # el total de registros es igual la longitud de cualquiera de las listas del diccionario
    # en el analisis no hemos asegurado de que todas las lineas del csv tengan el mismo numero de parametros, por lo que todas
    # las listas tienen la misma longitud
    totalRegistros = len(lista_datos)
    continue

# apartado B
for dato in datos["precio"]:
    precioMedio += float(dato)

precioMedio /= totalRegistros

# apartado C
for i, pais in enumerate( datos["destino"]):
        if pais in diccReservas:
            diccReservas[pais] += int(datos["unidades_reservadas"][i])
        else:
            diccReservas[pais] = int(datos["unidades_reservadas"][i])

for i, producto in enumerate( datos["producto"]):
        if producto in diccReservas:
            diccReservas[producto] += int(datos["unidades_reservadas"][i])
        else:
            diccReservas[producto] = int(datos["unidades_reservadas"][i])

for clave, n_reservas in diccReservas.items():
    if(n_reservas>MasVendido_unidades):
        MasVendido_unidades = n_reservas
        MasVendido = clave

# apartado D
for i, producto in enumerate( datos["producto"]):
        if producto in diccFacturacionProductos:
            diccFacturacionProductos[producto] += ( int(datos["unidades_reservadas"][i]) * float(datos["precio"][i]) )
        else:
            diccFacturacionProductos[producto] = ( int(datos["unidades_reservadas"][i]) * float(datos["precio"][i]) )




print("====================================================")
print()
print("ANÁLISIS EXPLORATORIO DE VENTAS - AGENCIA DE VIAJES")
print()
print("====================================================")
print(f"Numero total de registros: {totalRegistros}")
print(f"Precio medio de todos los paquetes/productos ofertados: {precioMedio}")
print(f"destino o producto más reservado, indicando el número total de unidades reservadas: {MasVendido} ({MasVendido_unidades} unidades)")
print("El importe total de facturación agrupado por tipo de producto:")
for producto, facturacion in diccFacturacionProductos.items():
    print(f" - {producto}: {facturacion}€")
