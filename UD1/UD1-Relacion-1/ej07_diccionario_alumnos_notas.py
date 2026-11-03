diccionario = {"Miguel":[1,9], "Jose Antonio":[6,8], "Alba":[5,2], "Jesus":[2,4], "Ruben":[4,5], "Antonio":[8,6], "Alvaro":[9,1]}
notas = 0
cont=0
for clave, valor in diccionario.items():
    for x in valor:
        notas = notas + x
        cont = cont + 1
media = notas/cont
print(f"la nota media de la clase es {media}")