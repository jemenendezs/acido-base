# Autor: Jorge Menéndez S.
# Licencia: MIT License
#
# Copyright (c) 2024 Jorge Menéndez S.
#
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para tratar
# en el Software sin restricciones, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y para permitir a las personas a quienes se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O
# LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD,
# YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE,
# FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL
# SOFTWARE.

def obtener_parametro(nombre):
    # Solicita un valor numérico al usuario y lo retorna.
    while True:
        try:
            valor = float(input(f"Ingrese el valor de {nombre}: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")

def determinar_trastorno_primario(pH, pCO2, HCO3):
    # Determina el trastorno ácido-base primario basado en pH, pCO2 y HCO3.
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

def calcular_compensacion(trastorno_primario, pCO2, HCO3, sodio, cloro):
    # Calcula la compensación esperada y los parámetros de compensación.
    resultados = []
    parametros_compensacion = {}

    if trastorno_primario == "Acidosis metabólica":
        pCO2_esperado_min = 1.5 * HCO3 + 8 - 2
        pCO2_esperado_max = 1.5 * HCO3 + 8 + 2
        anion_gap = sodio - (cloro + HCO3)
        delta_gap = anion_gap - 12
        delta_ratio = delta_gap / (HCO3 - 24)
        resultados.append(f"Compensación esperada por acidosis metabólica (Fórmula de Winters):")
        resultados.append(f"pCO2 esperado: {pCO2_esperado_min:.2f} a {pCO2_esperado_max:.2f} mmHg")
        resultados.append(f"Anion Gap: {anion_gap:.2f} mEq/L")
        resultados.append(f"Delta Gap: {delta_gap:.2f} mEq/L")
        resultados.append(f"Delta Ratio: {delta_ratio:.2f}")

        parametros_compensacion['pCO2'] = (pCO2_esperado_min, pCO2_esperado_max)

    elif trastorno_primario == "Acidosis respiratoria":
        HCO3_esperado_agudo_min = 24 + 0.1 * (pCO2 - 40) - 2
        HCO3_esperado_agudo_max = 24 + 0.1 * (pCO2 - 40) + 2
        HCO3_esperado_cronico_min = 24 + 0.35 * (pCO2 - 40) - 2
        HCO3_esperado_cronico_max = 24 + 0.35 * (pCO2 - 40) + 2
        resultados.append(f"Compensación esperada por acidosis respiratoria (agudo):")
        resultados.append(f"HCO3 esperado agudo: {HCO3_esperado_agudo_min:.2f} a {HCO3_esperado_agudo_max:.2f} mEq/L")
        resultados.append(f"Compensación esperada por acidosis respiratoria (crónico):")
        resultados.append(f"HCO3 esperado crónico: {HCO3_esperado_cronico_min:.2f} a {HCO3_esperado_cronico_max:.2f} mEq/L")

        parametros_compensacion['HCO3_agudo'] = (HCO3_esperado_agudo_min, HCO3_esperado_agudo_max)
        parametros_compensacion['HCO3_cronico'] = (HCO3_esperado_cronico_min, HCO3_esperado_cronico_max)

    elif trastorno_primario == "Alcalosis metabólica":
        pCO2_esperado_min = 0.7 * (HCO3 - 24) + 40 - 2
        pCO2_esperado_max = 0.7 * (HCO3 - 24) + 40 + 2
        resultados.append(f"Compensación esperada por alcalosis metabólica:")
        resultados.append(f"pCO2 esperado: {pCO2_esperado_min:.2f} a {pCO2_esperado_max:.2f} mmHg")

        parametros_compensacion['pCO2'] = (pCO2_esperado_min, pCO2_esperado_max)

    elif trastorno_primario == "Alcalosis respiratoria":
        HCO3_esperado_agudo_min = 24 - 2 * (40 - pCO2) - 2
        HCO3_esperado_agudo_max = 24 - 2 * (40 - pCO2) + 2
        HCO3_esperado_cronico_min = 24 - 4.5 * (40 - pCO2) - 2
        HCO3_esperado_cronico_max = 24 - 4.5 * (40 - pCO2) + 2
        resultados.append(f"Compensación esperada por alcalosis respiratoria (agudo):")
        resultados.append(f"HCO3 esperado agudo: {HCO3_esperado_agudo_min:.2f} a {HCO3_esperado_agudo_max:.2f} mEq/L")
        resultados.append(f"Compensación esperada por alcalosis respiratoria (crónico):")
        resultados.append(f"HCO3 esperado crónico: {HCO3_esperado_cronico_min:.2f} a {HCO3_esperado_cronico_max:.2f} mEq/L")

        parametros_compensacion['HCO3_agudo'] = (HCO3_esperado_agudo_min, HCO3_esperado_agudo_max)
        parametros_compensacion['HCO3_cronico'] = (HCO3_esperado_cronico_min, HCO3_esperado_cronico_max)

    return resultados, parametros_compensacion

def determinar_trastorno_secundario(pCO2, HCO3, parametros_compensacion, trastorno_primario):
    # Determina si hay un trastorno secundario basado en la compensación esperada.
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

def mostrar_resultados(trastorno_primario, resultados_compensacion, trastorno_secundario):
    # Muestra los resultados del análisis en un formato legible.
    print("\n" + "*"*50)
    print("RESULTADOS:")
    print(f"* Trastorno primario: {trastorno_primario}")
    print("\nCompensación esperada:")
    for resultado in resultados_compensacion:
        print(f"* {resultado}")
    print(f"\n* Trastorno secundario: {trastorno_secundario}")
    print("*"*50)

def main():
    # Función principal que coordina la ejecución del programa.
    print("Análisis ácido-base")
    pH = obtener_parametro("pH")
    pCO2 = obtener_parametro("pCO2")
    HCO3 = obtener_parametro("HCO3")
    sodio = obtener_parametro("Sodio")
    cloro = obtener_parametro("Cloro")

    trastorno_primario = determinar_trastorno_primario(pH, pCO2, HCO3)
    resultados_compensacion, parametros_compensacion = calcular_compensacion(trastorno_primario, pCO2, HCO3, sodio, cloro)
    trastorno_secundario = determinar_trastorno_secundario(pCO2, HCO3, parametros_compensacion, trastorno_primario)

    mostrar_resultados(trastorno_primario, resultados_compensacion, trastorno_secundario)

if __name__ == "__main__":
    main()
