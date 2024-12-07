class Video: 
    def __init__(self, duracion, formato):
        self.duracion = duracion
        self.formato = formato

    def informacionDetallada(self):
        print("-----------------------------")
        print("|Recurso:\t\t\t|Video\t\t\t|")
        print("|Duracion:\t\t\t|" + self.duracion + "\t\t\t|", "\n|Formato:\t\t\t|" + self.formato + "\t\t\t|")
        print("-----------------------------")