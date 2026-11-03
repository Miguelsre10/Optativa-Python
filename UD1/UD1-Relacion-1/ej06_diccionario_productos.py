diccionario = {"producto":1, "item":6, "cosa":7, "algo":2}

for clave, valor in diccionario.items():
    if valor < 5:
        print(f"\n{clave} tiene un valor menor a 5. Su valor es: {valor}")