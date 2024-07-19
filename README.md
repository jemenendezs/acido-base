# Estado ácido base
Este código realiza un análisis del estado ácido-base del paciente, evaluando tanto trastornos primarios como posibles trastornos secundarios basados en la compensación esperada. La presentación de los resultados es clara y estructurada para facilitar la interpretación de los datos.


### 1. **Función `obtener_parametro`**
```python
def obtener_parametro(nombre):
    # Solicita un valor numérico al usuario y lo retorna.
    while True:
        try:
            valor = float(input(f"Ingrese el valor de {nombre}: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")
```
- **Propósito**: Solicitar al usuario un valor numérico para diferentes parámetros (como pH, pCO2, HCO3, sodio, cloro).
- **Cómo lo hace**: Usa un bucle `while True` para seguir pidiendo el valor hasta que el usuario ingrese un número válido. Si se ingresa un valor no numérico, muestra un mensaje de error y solicita el valor nuevamente.

### 2. **Función `determinar_trastorno_primario`**
```python
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
```
- **Propósito**: Determinar el tipo de trastorno ácido-base primario basado en los valores de pH, pCO2 y HCO3.
- **Cómo lo hace**: 
  - Si el pH es menor a 7.35, se considera una acidosis. Si el pCO2 es alto, se clasifica como acidosis respiratoria; si no, como acidosis metabólica.
  - Si el pH es mayor a 7.45, se considera una alcalosis. Si el pCO2 es bajo, se clasifica como alcalosis respiratoria; si no, como alcalosis metabólica.
  - Si el pH está en el rango normal, se considera un trastorno indeterminado.

### 3. **Función `calcular_compensacion`**
```python
def calcular_compensacion(trastorno_primario, pCO2, HCO3, sodio, cloro):
    # Calcula la compensación esperada y los parámetros de compensación.
    resultados = []
    parametros_compensacion = {}
    ...
    # Cálculos específicos para cada trastorno primario
    return resultados, parametros_compensacion
```
- **Propósito**: Calcular la compensación esperada para el trastorno ácido-base primario y proporcionar los parámetros de compensación necesarios.
- **Cómo lo hace**:
  - **Acidosis metabólica**: Calcula el rango esperado para pCO2 usando la fórmula de Winters. También calcula el anion gap, delta gap y delta ratio si es necesario.
  - **Acidosis respiratoria**: Calcula el rango esperado para HCO3 en condiciones agudas y crónicas.
  - **Alcalosis metabólica**: Calcula el rango esperado para pCO2.
  - **Alcalosis respiratoria**: Calcula el rango esperado para HCO3 en condiciones agudas y crónicas.

### 4. **Función `determinar_trastorno_secundario`**
```python
def determinar_trastorno_secundario(pCO2, HCO3, parametros_compensacion, trastorno_primario):
    # Determina si hay un trastorno secundario basado en la compensación esperada.
    if trastorno_primario == "Acidosis metabólica":
        ...
    elif trastorno_primario == "Alcalosis metabólica":
        ...
    elif trastorno_primario == "Acidosis respiratoria":
        ...
    elif trastorno_primario == "Alcalosis respiratoria":
        ...
    return "No aplica"
```
- **Propósito**: Determinar si hay un trastorno secundario basado en la compensación observada en relación con la esperada.
- **Cómo lo hace**: Compara los valores medidos con los valores esperados para cada tipo de trastorno primario. Si los valores medidos están fuera del rango esperado, identifica un posible trastorno secundario.

### 5. **Función `mostrar_resultados`**
```python
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
```
- **Propósito**: Imprimir los resultados del análisis en un formato claro y organizado.
- **Cómo lo hace**: Imprime el trastorno primario, los resultados de la compensación esperada, y el posible trastorno secundario en un formato legible y bien separado.

### 6. **Función `main`**
```python
def main():
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
```
- **Propósito**: Ejecutar el flujo principal del programa.
- **Cómo lo hace**: Llama a las funciones para obtener parámetros del usuario, determinar el trastorno primario, calcular la compensación, identificar el trastorno secundario y mostrar los resultados.
