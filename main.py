from libro import Libro
from revista import Revista
from video import Video
from recursos import Recursos
from biblioteca import Biblioteca

biblioteca = Biblioteca()

def menu():
    print("Seleccione una opción:")
    print("1. Ingresar Recurso")
    print("2. Buscar Recurso")
    print("3. Eliminar Recurso")
    print("4. Listar Recursos")
    print("5. Prestar Recursos")
    print("6. Devolver Recurso")
    print("7. Salir")

def menu_ingresar_recurso():
    print("Ingrese los datos del recurso:")
    print("1. Libro")
    print("2. Revista")
    print("3. Video")
    print("4. Salir")

def menu_buscar_recurso():
    print("Seleccione una opción:")
    print("1. Buscar por autor")
    print("2. Buscar por tipo")
    print("4. Salir")


def main():
    while True:
        menu()
        opcion = input("Ingrese su opción: ")
        if opcion == '7':
            print("Saliendo del programa...")
            break
        elif opcion == '1':
            while True:
                menu_ingresar_recurso()
                opcion_ingresar_recurso = input("Ingrese su opción: ")
                if opcion_ingresar_recurso == '4':
                    break
                elif opcion_ingresar_recurso == '1':
                    titulo = input("Ingrese el titulo del libro: ")
                    autor = input("Ingrese el autor del libro: ")
                    anoPublicacion = input("Ingrese el año de publicación del libro: ")
                    genero = input("Ingrese el género del libro: ")
                    numeroPaginas = input("Ingrese el número de páginas del libro: ")
                    libro = Libro(genero, numeroPaginas)

                    recursoLibro = Recursos(libro, titulo, autor, anoPublicacion, libro)
                    
                    biblioteca.agregarRecurso(recursoLibro)
                elif opcion_ingresar_recurso == '2':
                    titulo = input("Ingrese el titulo de la revista: ")
                    autor = input("Ingrese el autor de la revista: ")
                    anoPublicacion = input("Ingrese el año de publicación de la revista: ")
                    numeroEdicion = input("Ingrese el número de edición de la revista: ")
                    frecuenciaPublicacion = input("Ingrese la frecuencia de publicación de la revista: ")
                    revista = Revista(numeroEdicion, frecuenciaPublicacion)

                    recursoRevista = Recursos(revista, titulo, autor, anoPublicacion, revista)

                    biblioteca.agregarRecurso(recursoRevista)
                
                elif opcion_ingresar_recurso == '3':
                    titulo = input("Ingrese el titulo del video: ")
                    autor = input("Ingrese el autor del video: ")
                    anoPublicacion = input("Ingrese el año de publicación del video: ")
                    duracion = input("Ingrese la duración del video: ")
                    formato = input("Ingrese el formato del video: ")
                    video = Video(duracion, formato)

                    recursoVideo = Recursos(video, titulo, autor, anoPublicacion, video)

                    biblioteca.agregarRecurso(recursoVideo)

                else:
                    print("Opción no válida, intente de nuevo.")

        elif opcion == '2':
            menu_buscar_recurso()
            opcion_buscar_recurso = input("Ingrese su opción: ")
            if opcion_buscar_recurso == '3':
                break
            elif opcion_buscar_recurso == '1':
                autor = input("Ingrese el autor del recurso: ")
                biblioteca.buscarPorAutor(autor)
            elif opcion_buscar_recurso == '2':
                tipo = input("Ingrese el tipo del recurso: ")
                biblioteca.buscarPorTipo(tipo)
            else:
                print("Opción no válida, intente de nuevo.")

        elif opcion == '3':
            print("Ha seleccionado Eliminar Recurso")
            tituloEliminar = input("Ingrese el titulo del recurso a eliminar: ")
            biblioteca.eliminarRecurso(tituloEliminar)

        elif opcion == '4':
            print("Ha seleccionado Listar Recursos")

            biblioteca.mostrarRecursosDisponibles()

        elif opcion == '5':
            print("Ha seleccionado Prestar Recursos")
            tituloPrestar = input("Ingrese el titulo del recurso a prestar: ")
            biblioteca.prestarRecurso(tituloPrestar)

        elif opcion == '6':
            print("Ha seleccionado Devolver Recurso")
            tituloDevolver = input("Ingrese el titulo del recurso a devolver: ")
            biblioteca.devolverRecurso(tituloDevolver)
            
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()