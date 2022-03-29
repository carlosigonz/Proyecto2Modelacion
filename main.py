from archivo import *
from tarea import *
def main():

    ruta_critica = []
    lista_tareas = []

    tareas = {1: Tarea(1, "A", 2, []),
              2: Tarea(2, "B", 3, [1]),
              3: Tarea(3, "E", 2, [1]),
              4: Tarea(4, "C", 1, [2,3]),
              5: Tarea(5, "D", 3, [3]),
              6: Tarea(6, "F", 2, [4,5]),
              7: Tarea(7, "G", 2, [6])
              }
    def ordenar_tareas(tareas, is_reverse=False):
        tareas_ordenadas = []

        keys_ordenados = sorted(tareas, reverse=is_reverse)

        for key in keys_ordenados:
            tareas_ordenadas.append(tareas[key])

        return tareas_ordenadas

    def forward_pass():
        for tarea in ordenar_tareas(tareas):
            tarea.asignar_predecesores(tareas)
            tarea.calcular_inicio_temprano()
            tarea.calcular_final_temprano()

    def backward_pass():
        nodo_final = True
        for tarea in ordenar_tareas(tareas, True):
            if nodo_final:
                tarea.final_tardio = tarea.final_temprano
                tarea.inicio_tardio = tarea.inicio_temprano
                nodo_final = False

            tarea.calcular_inicio_tardio()
            tarea.calcular_final_tardio()
            tarea.calcular_holgura()

            lista_tareas.append(tarea)
            if tarea.holgura == 0:
                ruta_critica.append(tarea)

    forward_pass()
    backward_pass()


    for i in lista_tareas[::-1]:
        print(f"\n----------Datos para la actividad {i.descripcion}----------")
        print(f"\nDía de inicio más temprano: {i.inicio_temprano}" )
        print(f"Día de inicio más tardío: {i.inicio_tardio}")
        print(f"Día de finalización más temprano: {i.final_temprano}")
        print(f"Día de finalización más tardío: {i.final_tardio}")

        if i.holgura > 0:
            print(f"La holgura de esta actividad es: {i.holgura}")
        else:
            print("Esta actividad no tiene holgura")

    ruta = "\n-La ruta crítica es: "
    for i in ruta_critica[::-1]:
        if i.final_tardio == ruta_critica[0].final_tardio:
            ruta = ruta +(f"{i.descripcion}.")
        else:
            ruta = ruta+(f"{i.descripcion}, ")
    print(ruta)
    print("-Duración máxima de días: ", ruta_critica[0].final_tardio, " días")

main()