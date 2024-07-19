def obtener_parametro(nombre):
    while True:
        try:
            valor = float(input(f"Ingrese el valor de {nombre}: "))
            return valor
        except ValueError:
            print(f"Entrada inválida. Por favor, ingrese un valor numérico para {nombre}.")

def determinar_trastorno_primario(pH, pCO2, HCO3):
    if pH < 7.35:
        if pCO2 > 45:
            return "Acidosis respiratoria"
        else:
            return "Acidosis metabólica"
    elif pH > 7.45:
        if pCO2 < 35:
            return "Alcalosis respiratoria"
        else:
            return "Alcalosis metabólica"
    else:
        return "Trastorno ácido-base indeterminado"

def calcular_compensacion(trastorno_primario, pCO2, HCO3):
    resultados = []
    parametros_compensacion = {}

    if trastorno_primario == "Acidosis metabólica":
        pCO2_esperado_min = 1.5 * HCO3 + 8 - 2
        pCO2_esperado_max = 1.5 * HCO3 + 8 + 2
        parametros_compensacion['pCO2'] = (pCO2_esperado_min, pCO2_esperado_max)
        resultados.append(f"Compensación esperada por acidosis metabólica (Fórmula de Winters):")
        resultados.append(f"pCO2 esperado: {pCO2_esperado_min:.2f} a {pCO2_esperado_max:.2f} mmHg")

    elif trastorno_primario == "Acidosis respiratoria":
        HCO3_esperado_agudo_min = 24 + 0.1 * (pCO2 - 40) - 2
        HCO3_esperado_agudo_max = 24 + 0.1 * (pCO2 - 40) + 2
        HCO3_esperado_cronico_min = 24 + 0.35 * (pCO2 - 40) - 2
        HCO3_esperado_cronico_max = 24 + 0.35 * (pCO2 - 40) + 2
        parametros_compensacion['HCO3_agudo'] = (HCO3_esperado_agudo_min, HCO3_esperado_agudo_max)
        parametros_compensacion['HCO3_cronico'] = (HCO3_esperado_cronico_min, HCO3_esperado_cronico_max)
        resultados.append(f"Compensación esperada por acidosis respiratoria (agudo):")
        resultados.append(f"HCO3 esperado agudo: {HCO3_esperado_agudo_min:.2f} a {HCO3_esperado_agudo_max:.2f} mEq/L")
        resultados.append(f"Compensación esperada por acidosis respiratoria (crónico):")
        resultados.append(f"HCO3 esperado crónico: {HCO3_esperado_cronico_min:.2f} a {HCO3_esperado_cronico_max:.2f} mEq/L")

    elif trastorno_primario == "Alcalosis metabólica":
        pCO2_esperado_min = 0.7 * (HCO3 - 24) + 40 - 2
        pCO2_esperado_max = 0.7 * (HCO3 - 24) + 40 + 2
        parametros_compensacion['pCO2'] = (pCO2_esperado_min, pCO2_esperado_max)
        resultados.append(f"Compensación esperada por alcalosis metabólica:")
        resultados.append(f"pCO2 esperado: {pCO2_esperado_min:.2f} a {pCO2_esperado_max:.2f} mmHg")

    elif trastorno_primario == "Alcalosis respiratoria":
        HCO3_esperado_agudo_min = 24 - 2 * (40 - pCO2) - 2
        HCO3_esperado_agudo_max = 24 - 2 * (40 - pCO2) + 2
        HCO3_esperado_cronico_min = 24 - 4.5 * (40 - pCO2) - 2
        HCO3_esperado_cronico_max = 24 - 4.5 * (40 - pCO2) + 2
        parametros_compensacion['HCO3_agudo'] = (HCO3_esperado_agudo_min, HCO3_esperado_agudo_max)
        parametros_compensacion['HCO3_cronico'] = (HCO3_esperado_cronico_min, HCO3_esperado_cronico_max)
        resultados.append(f"Compensación esperada por alcalosis respiratoria (agudo):")
        resultados.append(f"HCO3 esperado agudo: {HCO3_esperado_agudo_min:.2f} a {HCO3_esperado_agudo_max:.2f} mEq/L")
        resultados.append(f"Compensación esperada por alcalosis respiratoria (crónico):")
        resultados.append(f"HCO3 esperado crónico: {HCO3_esperado_cronico_min:.2f} a {HCO3_esperado_cronico_max:.2f} mEq/L")

    return resultados, parametros_compensacion

def determinar_trastorno_secundario(pCO2, HCO3, parametros_compensacion, trastorno_primario):
    if trastorno_primario == "Acidosis metabólica":
        if 'pCO2' in parametros_compensacion:
            pCO2_esperado_min, pCO2_esperado_max = parametros_compensacion['pCO2']
            if pCO2_esperado_min <= pCO2 <= pCO2_esperado_max:
                return "No aplica"
            else:
                return "Alcalosis respiratoria concomitante" if pCO2 < pCO2_esperado_min else "Acidosis respiratoria concomitante"
    
    elif trastorno_primario == "Alcalosis metabólica":
        if 'pCO2' in parametros_compensacion:
            pCO2_esperado_min, pCO2_esperado_max = parametros_compensacion['pCO2']
            if pCO2_esperado_min <= pCO2 <= pCO2_esperado_max:
                return "No aplica"
            else:
                return "Acidosis respiratoria concomitante" if pCO2 < pCO2_esperado_min else "Alcalosis respiratoria concomitante"
    
    elif trastorno_primario == "Acidosis respiratoria":
        if 'HCO3_agudo' in parametros_compensacion and 'HCO3_cronico' in parametros_compensacion:
            HCO3_esperado_agudo_min, HCO3_esperado_agudo_max = parametros_compensacion['HCO3_agudo']
            HCO3_esperado_cronico_min, HCO3_esperado_cronico_max = parametros_compensacion['HCO3_cronico']
            if HCO3_esperado_agudo_min <= HCO3 <= HCO3_esperado_agudo_max or HCO3_esperado_cronico_min <= HCO3 <= HCO3_esperado_cronico_max:
                return "No aplica"
            else:
                return "Acidosis metabólica concomitante" if HCO3 < HCO3_esperado_agudo_min else "Alcalosis metabólica concomitante"
    
    elif trastorno_primario == "Alcalosis respiratoria":
        if 'HCO3_agudo' in parametros_compensacion and 'HCO3_cronico' in parametros_compensacion:
            HCO3_esperado_agudo_min, HCO3_esperado_agudo_max = parametros_compensacion['HCO3_agudo']
            HCO3_esperado_cronico_min, HCO3_esperado_cronico_max = parametros_compensacion['HCO3_cronico']
            if HCO3_esperado_agudo_min <= HCO3 <= HCO3_esperado_agudo_max or HCO3_esperado_cronico_min <= HCO3 <= HCO3_esperado_cronico_max:
                return "No aplica"
            else:
                return "Acidosis metabólica concomitante" if HCO3 < HCO3_esperado_agudo_min else "Alcalosis metabólica concomitante"
    
    return "No aplica"

def main():
    # Obtener datos del usuario
    pH = obtener_parametro("pH")
    pCO2 = obtener_parametro("pCO2")
    HCO3 = obtener_parametro("HCO3")
    sodio = obtener_parametro("sodio")
    cloro = obtener_parametro("cloro")

    # Determinar el trastorno primario
    trastorno_primario = determinar_trastorno_primario(pH, pCO2, HCO3)

    # Calcular la compensación
    resultados_compensacion, parametros_compensacion = calcular_compensacion(trastorno_primario, pCO2, HCO3)

    # Determinar el trastorno secundario
    trastorno_secundario = determinar_trastorno_secundario(pCO2, HCO3, parametros_compensacion, trastorno_primario)

    # Mostrar resultados
    print("\n" + "*"*50)
    print("RESULTADOS:")
    print(f"* Trastorno primario: {trastorno_primario}")
    for resultado in resultados_compensacion:
        print(f"* {resultado}")
    print(f"* Trastorno secundario: {trastorno_secundario}")

if __name__ == "__main__":
    main()
