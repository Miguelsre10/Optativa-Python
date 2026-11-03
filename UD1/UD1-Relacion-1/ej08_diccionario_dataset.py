def analisis(datos, min, max):
    filtrado={}
    numVal=0
    for ci, vi in datos.items():
        for cj, vj in vi.items():
            for ck, vk in vj.items():
                if vk >= min and vk <= max:
                    filtrado[f"{ci}-{cj}-{ck}"]=vk
                    numVal = numVal + 1

    return (filtrado, numVal)

datos = {
      #ci
    "Enero": {
           #cj          #ck    #vk
        "Facebook": {"clics": 3400, "impresiones": 150000, "conversiones": 120},
        "Instagram": {"clics": 4100, "impresiones": 170000, "conversiones": 150},
        "Twitter": {"clics": 900, "impresiones": 60000, "conversiones": 45}
    },
    "Febrero": {
        "Facebook": {"clics": 3200, "impresiones": 140000, "conversiones": 110},
        "Instagram": {"clics": 3900, "impresiones": 160000, "conversiones": 140},
        "Twitter": {"clics": 950, "impresiones": 58000, "conversiones": 50}
    },
    "Marzo": {
        "Facebook": {"clics": 3700, "impresiones": 155000, "conversiones": 130},
        "Instagram": {"clics": 4300, "impresiones": 175000, "conversiones": 160},
        "Twitter": {"clics": 1000, "impresiones": 62000, "conversiones": 55}
    }
}

#filtrado, numVal = analisis(datos, 10, 150)
filtrado, numVal = analisis(datos, 1000, 3900)

for clave, valor in filtrado.items():
    print(f"{clave} - {valor}\n")

print (f"se han filtrado {numVal} datos")


