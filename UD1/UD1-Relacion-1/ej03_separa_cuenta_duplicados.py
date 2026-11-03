def separador(lista):
    unicos= list(())
    repeticiones = list(())

    for i in lista:
        if i in unicos:
            repeticiones[unicos.index(i)] = repeticiones[unicos.index(i)] + 1
            #print(unicos.index(i))
        else:
            unicos.append(i)
            repeticiones.append(1)
    return unicos, repeticiones
    #return (unicos, repeticiones)

    
lista = [4, 5, 2, 3, 6, 1, 7, 1, 3, 2, 4, 5, 2, 1, 3, 5, 9, 8, 4, 4, 3, 2, 1, 7, 7, 1, 3, 9]
#lista = [1, 2, 2, 3, 3, 3, 3, 3, 2, 2, 1]

#u = separador(lista)
#unicos = u[0]
#repeticiones = u[1]

unicos, repeticiones = separador(lista)

for i in range(len(unicos)):
    print(unicos[i], ": " , repeticiones[i] , " repeticiones", sep="")
print(unicos)
print(repeticiones)
