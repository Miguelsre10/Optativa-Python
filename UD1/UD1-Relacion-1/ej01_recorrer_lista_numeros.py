lista = []
pares = []
continua = True
contt = 0
while continua:
    lista.append(int(input("introduce un numero: ")))
    contt += 1
    if contt >= 10:
        continua = False
        r = input("Quiere continuar introduciendo numeros? (y/n)")
        if r.lower() == "y":
            continua = True
        elif r.lower() == "n":
            continua = False
    

for n in lista:
    if n%2 == 0:
        pares.append(n)

if len(pares) == 0:
    print ("No hay numeros pares")
else:
    print(pares)

print(lista)

