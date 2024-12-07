class Biblioteca:
    def __init__(self):
        self.recursos = []

    def agregarRecurso(self, recurso):
        self.recursos.append(recurso)
    
    def mostrarRecursosDisponibles(self):
        for recurso in self.recursos:
            recurso.informacionDetallada()

    def buscarPorAutor(self, autor):
        for recurso in self.recursos:
            if recurso.autor == autor:
                recurso.informacionDetallada()

    def buscarPorTipo(self, tipo):
        for recurso in self.recursos:
            if recurso.tipo == tipo:
                recurso.informacionDetallada()
    
    def eliminarRecurso(self, recurso):
        for recurso in self.recursos:
            if recurso.titulo == recurso:
                if recurso.disponibilidad == False:
                    print("No se puede eliminar el recurso porque esta prestado")
                    return
                self.recursos.remove(recurso)
                print("Recurso eliminado")
                return
        print("No se encontro el recurso")
    
    def prestarRecurso(self, recurso):
        for recurso in self.recursos:
            if recurso.titulo == recurso:
                recurso.prestar()
                return
        print("No se encontro el recurso")

    def devolverRecurso(self, recurso):
        for recurso in self.recursos:
            if recurso.titulo == recurso:
                recurso.devolver()
                return
        print("No se encontro el recurso")

    
