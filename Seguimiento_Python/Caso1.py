# Hay diferentes formas de representar los datos, y cada forma
# tiene su propia forma de recorrerlos para procesarlos
# Resuelva los siguientes casos, donde la variable 'notas' contiene
# las notas de los 3 parciales para 3 materias de un mismo estudiante
# Recuerde:
# - Analice primero, planee/diseñe una solución, luego escriba el código
# - Utilice comentarios para explicar las partes importantes
# - Si es el caso utilice constantes
# - Realice sus propias pruebas para verificar que todo funciona

#Caso 1 Listas de listas

def calcular_nota_final(notas):
    notas_finales = [] #En esta variable guardamos como una lista los valores de las notas finales
    for materia in notas:
        nombre = materia[0]
        nota1 = materia[1]
        nota2 = materia[2]
        nota3 = materia[3]
        
        # se calcula la nota final según los porcentajes y llamando los valores almacenados en la lista
        nota_final = (0.3 * nota1) + (0.3 * nota2) + (0.4 * nota3)
        notas_finales.append((nombre, nota_final))
    
    return notas_finales

def calcular_promedio(notas_finales):
    suma_notas = sum(nota[1] for nota in notas_finales)
    promedio = suma_notas / len(notas_finales)
    return promedio

# Lista de listas con las materias y valores
notas = [ 
    ["Calculo", 3.5, 2.5, 1.5],
    ["Química", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Lógica", 1.5, 4.0, 4.5]
]

# Cálculo de las notas finales usando la variable de almacenamiento de listas
notas_finales = calcular_nota_final(notas)

# Cálculo del promedio usando la variable de almacenamiento de listas
promedio = calcular_promedio(notas_finales)

print("Notas finales:", notas_finales)
print("Promedio general del estudiante:", promedio)










