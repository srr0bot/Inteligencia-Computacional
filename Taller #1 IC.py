#!/usr/bin/env python3

import math

class Tarea:
    def __init__(self, costos):
        self.costos = costos  # Lista de costos para cada trabajador

def poda_alfa_beta(tareas, asignacion_actual, costo_actual, alfa, beta, es_maximizador):
    if not tareas:
        # No quedan tareas por asignar, retorna el costo acumulado actual.
        return costo_actual

    if es_maximizador:
        # Maximización
        valor_max = -math.inf
        for i, tarea in enumerate(tareas):
            for j, costo in enumerate(tarea.costos):
                if asignacion_actual[j] is None:
                    # Asignar la tarea al trabajador j
                    asignacion_actual[j] = i
                    nuevo_costo = costo_actual + costo
                    # Llamada recursiva para explorar la asignación actualizada
                    valor_max = max(valor_max, poda_alfa_beta(tareas[:i] + tareas[i+1:], asignacion_actual, nuevo_costo, alfa, beta, False))
                    # Actualizar alfa y realizar poda alfa-beta
                    alfa = max(alfa, valor_max)
                    asignacion_actual[j] = None  # Deshacer la asignación para retroceder
                    if beta <= alfa:
                        break  # Poda alfa-beta
        return valor_max
    else:
        # Minimización
        valor_min = math.inf
        for i, tarea in enumerate(tareas):
            for j, costo in enumerate(tarea.costos):
                if asignacion_actual[j] is None:
                    # Asignar la tarea al trabajador j
                    asignacion_actual[j] = i
                    nuevo_costo = costo_actual + costo
                    # Llamada recursiva para explorar la asignación actualizada
                    valor_min = min(valor_min, poda_alfa_beta(tareas[:i] + tareas[i+1:], asignacion_actual, nuevo_costo, alfa, beta, True))
                    # Actualizar beta y realizar poda alfa-beta
                    beta = min(beta, valor_min)
                    asignacion_actual[j] = None  # Deshacer la asignación para retroceder
                    if beta <= alfa:
                        break  # Poda alfa-beta
        return valor_min

if __name__ == "__main__":

    # Creamos instancias de tareas con costos asociados

    tarea1 = Tarea([2, 3, 1, 5])
    tarea2 = Tarea([5, 2, 4, 7])
    tarea3 = Tarea([1, 6, 2, 4])

    tareas = [tarea1, tarea2, tarea3]

    # Representa la asignación inicial de tareas a trabajadores
    asignacion_inicial = [None] * len(tarea1.costos)

    # Maximizar o minimizar
    opcion = input("¿Quieres maximizar o minimizar el costo? (max/min): ").lower()

    # Determina si se maximiza o minimiza
    es_maximizador = True if opcion == 'max' else False

    # Aplicamos el algoritmo de poda alfa-beta
    resultado = poda_alfa_beta(tareas, asignacion_inicial, costo_actual=0, alfa=-math.inf, beta=math.inf, es_maximizador=es_maximizador)

    # Resultado
    if es_maximizador:
        print("El costo máximo es:", resultado)
    else:
        print("El costo mínimo es:", resultado)
