def contar_elemento(tupla, elemento):
    contador = 0
    for x in tupla:
        if isinstance(x, tuple):
            contador += contar_elemento(x, elemento)
        else:
            if x == elemento:
                contador += 1
    return contador

def cuenta(tupla):
    num = 0
    cadena = 0
    booleano = 0
    unicos = 0

    for i in tupla:
        for j in i:
            #print("\nelemento:",j)
            if(contar_elemento(tupla, j) == 1):
                #print("unico")
                unicos = unicos + 1
            if(type(j) == int):
                num = num + 1
            elif(type(j) == str):
                cadena = cadena + 1
            elif(type(j) == bool):
                booleano = booleano + 1
    print("Hay", unicos, " elementos unicos")

    return (num, cadena, booleano)

tupla = (-2,"string", True),(1,True,4),(False, 0, -2)
#,("string",-7, "string")
#,("string",1, True),(True,5,4),( "cadena", True, "cadena"),( False,4 ,"cadena" ),("cadena" , "cadena", False),( False, 4,False ),(4 ,False ,"cadena" )

conteo = cuenta(tupla)


for i in range(len(conteo)):
    if(i == 0):
        print("hay", conteo[i] , "numeros")
    elif(i == 1):
        print("hay", conteo[i] , "cadenas")
    elif(i == 2):
        print("hay", conteo[i] , "bool")

