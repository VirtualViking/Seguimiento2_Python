#Caso2 Diccionario de listas

def calcular_notas(notas):
    # Lista de almacenamiento con los valores de cada corte
    valores = [0.3, 0.3, 0.4]
    
    # Diccionario donde se almacena las notas finales por materia
    notas_finales = {}
    
    # Calcular la nota final por materia
    for materia, calificaciones in notas.items():
        nota_final = sum(calificaciones[i] * valores[i] for i in range(len(calificaciones)))
        notas_finales[materia] = nota_final
    
    # Calcular el promedio general
    promedio_general = sum(notas_finales.values()) / len(notas_finales)
    
    # Retornar resultados en una tupla
    return notas_finales, promedio_general

# Ejemplo de uso
notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Química": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Lógica": [1.5, 4.0, 4.5]
}

resultados = calcular_notas(notas)
print("Notas finales por materia:", resultados[0]) 
print("Promedio general del estudiante:", resultados[1]) # Se llama la tupla promedio general donde se almaceno el resultado de las notas









