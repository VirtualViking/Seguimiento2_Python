
# Caso 3 Diccionario de diccionario
def calcular_notas(notas):
    
    ## Lista de almacenamiento con los valores de cada corte

    valores = {"pp": 0.3, "sp": 0.3, "tp": 0.4}
    
    # Usare este Diccionario para almacenar las notas finales de cada materia
    notas_finales = {}
    
    # Calculare la nota final por materia
    for materia, calificaciones in notas.items():
        nota_final = sum(calificaciones[parcial] * valores[parcial] for parcial in calificaciones)
        notas_finales[materia] = nota_final
    
    # Calculare el promedio de todas las notas finales
    promedio_general = sum(notas_finales.values()) / len(notas_finales)
    
    return notas_finales, promedio_general

notas = {
    "Calculo": {"pp": 3.5, "sp": 2.5, "tp": 1.5}, 
    "Química": {"pp": 2.5, "sp": 3.0, "tp": 5.0}, 
    "Deporte": {"pp": 2.4, "sp": 2.0, "tp": 2.2}, 
    "Lógica": {"pp": 1.5, "sp": 4.0, "tp": 4.5}
}

# Se llama la funcion y el diccionario que almaceno el valor de las notas de las materias desde un diccionario
notas_finales, promedio_general = calcular_notas(notas)
print("Notas finales por materia:", notas_finales)
print("Promedio general del estudiante:", promedio_general)



