import csv
media_temp = 0
contador_temp = 0
with open('./Python/UD1/UD1-Relacion-2/datos_temperatura.csv', mode='r') as f:
    lector = csv.reader(f, delimiter=',') #delimiter por defecto es ','
    #saltamos las cabeceras | es igual a hacer next(f) antes del csv.reader
    lector.__next__()
    
    #lista de string con los valores de la linea 
    for linea in lector:
        print(linea[1])
        media_temp += float(linea[1])
        contador_temp += 1

    media_temp /= contador_temp

    print(f"La media de temperaturas es {media_temp}")