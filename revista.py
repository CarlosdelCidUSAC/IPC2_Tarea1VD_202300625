class Revista: 
    def __intit__(self, numeroEdicion, frecuenciaPublicacion):
        self.numeroEdicion = numeroEdicion
        self.frecuenciaPublicacion = frecuenciaPublicacion

    def informacionDetallada(self):
        print("-----------------------------")
        print("|Recurso:\t\t\t|Revista\t\t\t|")
        print("|Numero de edicion:\t\t\t|" + self.numeroEdicion + "\t\t\t|", "\n|Frecuencia de publicacion:\t" + self.frecuenciaPublicacion + "\t\t\t|")
        print("-----------------------------")
        