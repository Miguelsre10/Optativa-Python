"Examen UD1 - Optativa de Programacion Python aplicado a la inteligencia artificial"
"Autor/a: Miguel San Roman Espejo"
"Fecha: 10/11/2026"
"SOLUCIÓN"
"***************************************************************************************************************"

fichero = "ventas_tienda.csv"
salida =  "SEM_Solucion.txt"

#{producto: [], categoria:[]}
informacion = {}
listaClaves = []

numero_productos = 0
precio_medio = 0.0
productoMasVendido = ''
productoMasVendido_cantidad = 0
diccionario_categorias_ventas = {}

#con with open()  los ficheros se cierran solos al salir del bloque de codigo
#abrimos en modo de lectura
with open(fichero, "r") as f:


    #Ejercicio A
    for numero, linea in enumerate(f):
        #separamos los valores de la fila
        parametros = linea.strip().split(',')
        #si estamos en la primera fila los valores son las cabeceras de las columnas
        if(numero == 0):
            for clave in parametros:
                informacion[clave] = []
                listaClaves.append(clave)

        else:
            for i, dato in enumerate(parametros):
                informacion[listaClaves[i]].append(parametros[i])

    print(informacion)


    #Ejercicio B
    for clave, lista in informacion.items():
        #calculamos total de registros
        if clave == 'producto':
            numero_productos=len(lista)
            print("a)   Numero de productos registrados")
            print(numero_productos)

        #calculamos la media del precio
        if clave == "precio":
            media = 0
            for precio in lista:
                media += float(precio)

            precio_medio = media / len(lista)
            print("b)  El precio medio de todos los productos es")
            print(precio_medio)

        #comprobamos el producto mas vendido    
        if clave == "producto":
            #ponemos el primer producto de la lista para empezar la comprobacion
            productoMasVendido = informacion['producto'][i]
            productoMasVendido_cantidad = int(informacion['unidades_vendidas'][0])

            for i, producto in enumerate(lista):
                if productoMasVendido_cantidad < int(informacion['unidades_vendidas'][i]):
                    productoMasVendido = informacion['producto'][i]
                    productoMasVendido_cantidad = int(informacion['unidades_vendidas'][i])
                    
            print(f"c)  El producto mas vendido es {productoMasVendido}")
            print(f"Con {productoMasVendido_cantidad} unidades vendidas")

        #calculamos el importe de ventas total por categoria
        if clave == "categoria":
            
            for i, categoria in enumerate(lista):
                if categoria in diccionario_categorias_ventas:
                    diccionario_categorias_ventas[categoria] += float(informacion['precio'][i])*float(informacion['unidades_vendidas'][i])
                else:
                    diccionario_categorias_ventas [categoria] = float(informacion['precio'][i])*float(informacion['unidades_vendidas'][i])

            print("d)  Ventas por categoria")
            print(diccionario_categorias_ventas)

    #imprimimos por pantalla el resumen de la informacion
    print(f"Número total de productos: {numero_productos}'\n")
    print(f"Precio medio: {precio_medio}$'\n")
    print(f"Producto mas vendido: {productoMasVendido}({productoMasVendido_cantidad} unidades)\n")
    print(f"Importe total por categoria:\n")
    for categoria, valor in diccionario_categorias_ventas.items():
        print(f" - {categoria}: {valor}$\n")

    # Ejercicio D
    with open(salida, "w") as s:
        s.write(f"Número total de productos: {numero_productos}\n")
        s.write('\n')
        s.write(f"Precio medio: {precio_medio}$'\n")
        s.write('\n')
        s.write(f"Producto mas vendido: {productoMasVendido}({productoMasVendido_cantidad} unidades)\n")
        s.write('\n')
        s.write(f"Importe total por categoria:\n")
        s.write('\n')
        for categoria, valor in diccionario_categorias_ventas.items():
            s.write(f" - {categoria}: {valor}$\n")
            s.write('\n')
