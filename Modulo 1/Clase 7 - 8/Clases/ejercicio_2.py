def calcular_estadisticas(numeros):
    if not numeros:
        return "La lista esta vacia"
    estadisticas = {
        "suma": sum(numeros),
        "promedio": sum(numeros) / len(numeros),
        "maximo": max(numeros),
        "minimo": min(numeros),
        "cantidad": len(numeros)
        
    }
    return estadisticas

numeros = [10,23,25,69,70,90]
resultados = calcular_estadisticas(numeros)

for resultado in resultados:
    print(f"{resultado} : {resultados[resultado]}")

for clave, valor in resultados.items():
    print(clave, valor)