class Recursos:
    def __init__(self, valor, titulo, autor, anoPublicacion, disponibilidad):
            self.titulo = titulo
            self.autor = autor
            self.anoPublicacion = anoPublicacion
            self.disponibilidad = disponibilidad
            self.valor = valor

    def informacionDetallada(self):
        self.valor.informacionDetallada()

    def prestar(self):
        self.cabeza.disponibilidad = False

    def devolver(self):
        self.cabeza.disponibilidad = True



    
