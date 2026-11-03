def analisisCorpus(corpus):
    lpalabras={}
    cont = 0
    nletras = 0
    for i in corpus:
        cont = cont + 1
        lon = len(i)
        nletras = nletras + lon
        if lon in lpalabras:
            lpalabras[lon].append(i)
        else:
            lpalabras[lon] = [i]
    return( dict(sorted(lpalabras.items())), cont, nletras)


corpus=["en", "lingüística", "un", "corpus", "es", "conjunto", "de", "fragmentos", "textos", "orales",
        "o", "escritos", "producidos", "condiciones", "naturales", "conjuntamente", "representativos",
        "una", "lengua", "variedad", "su", "totalidad", "algunos", "sus", "componentes", "que", "se",
        "almacenan", "formato", "electrónico", "y", "codifican","anotan", "con", "la", "intención",
        "puedan", "ser", "analizados", "científicamente", "esta", "definición", "destaca", "todos",
        "los", "aspectos", "relevantes", "este", "tipo", "recursos"
]

lp, cont, nletras = analisisCorpus(corpus)

for cp, vp in lp.items():
    st = f"{cp} letras: "
    for i in vp:
        st = st + f"{i} "
    print(st)

print(f"Se han procesado {cont} palabras")
print(f"La longitud promedio es {nletras/cont}")
