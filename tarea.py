class Tarea():
    def __init__(self, id, descripcion, duracion, predecesores_id):
        self.id = id
        self.duracion = duracion
        self.descripcion = descripcion
        self.predecesores_id = predecesores_id
        self.inicio_temprano = None
        self.final_temprano = None
        self.inicio_tardio = None
        self.final_tardio = None
        self.holgura = None
        self.predecesores= {}


    def asignar_predecesores(self, tareas):
        for id_predecesor in self.predecesores_id:
            self.predecesores[id_predecesor] = tareas[id_predecesor]

    def calcular_inicio_temprano(self):
        if len(self.predecesores) == 0:
            self.inicio_temprano = 0
            self.calcular_final_temprano
        else:
            temp = 0
            for id_predecesor in self.predecesores:

                predecesor = self.predecesores[id_predecesor]

                if predecesor.final_temprano > temp:
                    temp = predecesor.final_temprano

            self.inicio_temprano = temp




    def calcular_final_temprano(self):
        self.final_temprano = self.inicio_temprano + self.duracion

    def calcular_inicio_tardio(self):
        self.inicio_tardio = self.final_tardio - self.duracion

    def calcular_final_tardio(self):
        for id_predecesor in self.predecesores:
            predecesor = self.predecesores[id_predecesor]
            if predecesor.final_tardio == None:
                predecesor.final_tardio = self.inicio_tardio
            if predecesor.final_tardio >= self.inicio_tardio:
                predecesor.final_tardio = self.inicio_tardio

    def calcular_holgura(self):
        self.holgura = self.inicio_tardio - self.inicio_temprano
