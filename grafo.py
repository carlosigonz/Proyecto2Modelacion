import csv
import networkx as nx
import matplotlib.pyplot as plt


def leerNodos(archivo):
    listaNombre = []
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            listaNombre.append(row[0])
    return listaNombre


def leerAristas(archivo):
    listaAristas = []
    auxiliar = []
    auxiliar2 = []
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:

            auxiliar = row[3].split(",")

            for aux in auxiliar:

                #print("Arista inicial", row[0], "Combinada con", aux)
                auxiliar2.append(row[0])
                auxiliar2.append(aux)
            # print(auxiliar2)
                listaAristas.append(auxiliar2)
                auxiliar2 = []

    return listaAristas