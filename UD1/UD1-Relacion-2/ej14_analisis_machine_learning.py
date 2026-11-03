def leer_metricas(fichero):
    resultado = {}
    with open(fichero, "r") as f:
        for line in f:
            parametro = line.strip().split(',')
            #[0]: modelo1 | [1]: accuracy | [1]: 0.85
            if parametro[0] in resultado:
                resultado[parametro[0]][parametro[1]] = parametro[2]
                #{"machine1": {"accuracy": 0.85, "loss":0.20}}
            else:
                resultado[parametro[0]] =  {parametro[1] : parametro[2]}
                #{"machine1": {"accuracy": 0.85}}
                
    #print(res)
    return resultado

def analizar_metricas(dic_metricas):
    accuracy = 0
    loss = 0
    max_acc_machine = None
    for modelo, metricas in dic_metricas.items():
        for metrica, valor in metricas.items():
            #print(modelo)
            #print(metrica)
            #print(valor)
            if metrica == "accuracy":
                accuracy += float(valor)
            if metrica == "loss":
                loss += float(valor)

            if metrica == "accuracy":
                if max_acc_machine is None:
                    max_acc_machine = dict(maxx_acc = modelo)
                    max_acc_value = float(valor)
                elif max_acc_value < float(valor):
                    max_acc_machine = dict(maxx_acc = modelo)
                    max_acc_value = float(valor)

    avg_loss = loss / len(modelo)
    avg_accuracy = accuracy / len(modelo)

    print(f"average loss: {avg_loss}")
    print(f"average accuracy: {avg_accuracy}")
    print(f"maximum accuracy: {max_acc_machine}")



analizar_metricas(leer_metricas("./Python/UD1/UD1-Relacion-2/metricas.txt"))