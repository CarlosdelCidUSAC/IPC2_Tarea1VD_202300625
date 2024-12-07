class Libro:
    def __init__(self, genero, numeroPaginas):
        self.genero = genero
        self.numeroPaginas = numeroPaginas

    def informacionDetallada(self):
        print("-----------------------------")
        print("|Recurso:\t\t\t|Libro\t\t\t|")
        print("|Genero:\t\t\t|" + self.genero + "\t\t\t|", "\n|Numero de paginas:\t\t|" + self.numeroPaginas + "\t\t\t|")
        print("-----------------------------")