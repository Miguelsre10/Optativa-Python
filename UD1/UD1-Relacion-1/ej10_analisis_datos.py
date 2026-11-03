def conversion_promedio(datos):
    conv = {}
    for mes, dicc_plat in datos.items():
        for plat, dicc_metricas in dicc_plat.items():
            for metrica, valor in dicc_metricas.items():
                if metrica=="conversiones":
                    if plat in conv:
                        conv[plat] = conv[plat] + valor
                    else:
                        conv[plat] = valor

    print(f"La conversion promedio por plataforma es:")
    for plataforma, valor in conv.items():
        conv[plataforma] = conv[plataforma] / len(datos)
    #    print(f"\t{ci}: {conv[ci]}")   
    return conv
    
def analisis_ctr(datos):
    ctr = {}
    fctr = {}
    tctr = {}
    ictr = {}
    for mes, vi in datos.items():
        for plat, dicc_metricas in vi.items():
            if plat == "Facebook":
                fctr[mes] = dicc_metricas["clics"]/dicc_metricas["impresiones"]
            elif plat == "Instagram":
                ictr[mes] = dicc_metricas["clics"]/dicc_metricas["impresiones"]
            elif plat == "Twitter":
                tctr[mes] = dicc_metricas["clics"]/dicc_metricas["impresiones"]
    ctr["Facebook"] = fctr
    ctr["Instagram"] = ictr
    ctr["Twitter"] = tctr
    return ctr

# ratio de conversion de clicks
def ratio_conv_clic(datos):
    conv = conversion_promedio(datos)
    conv_clic = {}
    clics = {}
    for mes, dicc_plat in datos.items():
        for plat, dicc_metricas in dicc_plat.items():
            for metrica, valor in dicc_metricas.items():
                if metrica=="clics":
                    if plat in clics:
                        clics[plat] = clics[plat] + valor
                    else:
                        clics[plat] = valor

    for plat, valor in clics.items():
        conv_clic[plat] = conv[plat]*3 / clics[plat]

    mayor = []
    mayor.append(next(iter(conv_clic)))
    mayor.append(conv_clic[mayor[0]])

    for plat, valor in conv_clic.items():
        if valor > mayor[1]:
            mayor[0] = plat
            mayor[1] = valor

    print(f"{mayor[0]} fue la plataforma con el mejor ratio de conversiones por clic con {mayor[1]}")
    return mayor

    
def mas_conv(datos):
    convt = {}
    for mes, dicc_plat in datos.items():
        for plat, dicc_metricas in dicc_plat.items():
            for metrica, valor in dicc_metricas.items():
                if metrica=="conversiones":
                    if mes in convt:
                        convt[mes] = convt[mes] + valor
                    else:
                        convt[mes] = valor

    mayor = []
    mayor.append(next(iter(convt)))
    mayor.append(convt[mayor[0]])

    for mes, valor in convt.items():
        if valor > mayor[1]:
            mayor[0] = mes
            mayor[1] = valor

    print(f"{mayor[0]} fue el mes con el mayor número total de conversiones sumando todas las plataformas con {mayor[1]}")
    return mayor    
    

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
conv_prom=conversion_promedio(datos)
print("\nConversion promedio por plataforma")
print(conv_prom)
print("\nCTR")
print(analisis_ctr(datos))
print("\nRatio de conversiones por click")
ratio_conv_clic(datos)
print("\nMayor total de conversiones por click")
mas_conv(datos)
