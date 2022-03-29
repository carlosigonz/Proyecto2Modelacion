from tarea import Tarea
import csv

tareas = {}
indice_tareas = {}
lista_tareas = []

def leer_tareas(archivo):
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        cuenta = 0
        for row in csv_reader:
            identif = row[0]
            if identif == 'ï»¿1':
                identif = 1
            identif = int(identif)
            descrip = row[1]
            duracion = row[2]
            duracion = int(duracion)
            predec = predec_ids(row[3])
            nueva_tarea = Tarea(identif,descrip,duracion,predec)
            tareas[nueva_tarea.id] = nueva_tarea
            lista_tareas.append(identif)
            # for i in grafo:
            #     i.append(0)
            # grafo.append([0] * (len(grafo) + 1))
            indice_tareas[nueva_tarea] = len(indice_tareas)
            cuenta += 1
        print(f'Se agregaron {cuenta} tareas')
        # print(tareas)
        # for x in tareas:
        #     nodo = tareas[x]
        #     print(nodo.id)
        #     print(nodo.descripcion)
        #     print(nodo.duracion)
        #     print(nodo.predecesores_id)

def predec_ids(id):
    lista_ids= []
    predec_ids_string = id.split(',')
    for id in predec_ids_string:
        if id != '':
            id = int(id)
            lista_ids.append(id)
    return lista_ids