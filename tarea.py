class Tarea:
    def __init__(self, numero, descripcion, duracion, predecesor):
        self.nombre = numero
        self.descripcion = descripcion
        self.duracion = duracion
        self.predecesor = predecesor
        self.early_start = None
        self.early_finish = None
        self.late_start = None
        self.late_finish = None
        self.holgura = None
