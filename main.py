from libro import Libro
from usuario import Usuario
from empleado import Empleado


lista_de_usuarios=[]
lista_de_empleados=[]
lista_de_libros=[]
def menu_ingreso():

    while True:
        opcion = int(input(' Menu\n----------\t'+
                       '\n\t1. Añadir nuevo libro'
                       '\n\t2. Ver lista de libros'
                       '\n\t3. Buscar libro por título'
                       '\n\t4. Buscar libro por ID'
                        '\n\t5. Buscar libro por Autor'
                        '\n\t6. Buscar libro por año'
                        '\n\t7. Buscar libro por Genero'
                       '\n\t8. Inscribir usuario'
                       '\n\t9. Inscribir empleado'
                       '\n\t10. Eliminar libros'
                       '\n\t11. Reservar libro'
                       '\n\t12. Filtrar libros'
                       '\n\t13. Modificar atributos del libro'
                       '\n\t14. Prestamo de libro'
                       '\n\t15. Devolución de libro'
                       '\n\t16. Generar informe'
                       '\n\t17. Salir del sistema'
                       '\nIngrese la opcion que desea:\n'))

        if opcion ==1:
           anadir_libro()
        elif opcion ==2:
            mostrar_lista_libros()
        elif opcion ==3:
            buscar_libro("titulo")
        elif opcion ==4:
            buscar_libro("id")
        elif opcion== 5:
            pass
        elif opcion ==4:
            crear_usuario()
            print('Usuario inscrito')
        elif opcion ==5:
            print('Empleado instrito')
        elif opcion ==6:
            eliminar_libro()
        elif opcion ==7:
            print('Libro reservado')
        elif opcion ==8:
            print('Atributos modificados')
        elif opcion ==9:
            print('Atributos modificados')
        elif opcion ==10:
            print('Préstamo realizado')
        elif opcion ==11:
            print('Libro devuelto')
        elif opcion ==12:
            print('Informe generado')
        elif opcion==13:
            break
        else:
            print('¡Opción no valida!')


def crear_usuario():
    cedula=input("Ingrese su numero de cedula: ")
    nombre=input("Ingrese su nombre: ")
    apellido1=input("Ingrese su primer apellido: ")
    apellido2=input("Ingrese su segundo apellido: ")
    direccion=input("Ingrese su direccion: ")
    telefono=input("Ingrese su numero de telefono: ")

    objUsuario=Usuario(cedula,nombre,apellido1,apellido2,direccion,telefono)
    lista_de_usuarios.append(objUsuario)
    print("Usuario: "+ nombre + " agregado correctamente.")

def crear_empleado():
    cedula = input('Ingrese el número de cédula: ')
    nombre = input('Ingrese el primer apellido: ')
    apellido1 = input('Ingrese el primer apellido: ')
    apellido2 = input('Ingrese el segundo apellido: ')
    codigo_empleado = input('Ingrese el código de empleado: ')
    puesto = input('Ingrese el puesto: ')

    ObjEmpleado=Empleado(cedula,nombre,apellido1,apellido2,codigo_empleado,puesto)
    lista_de_empleados.append(ObjEmpleado)
    print('El empleado'+nombre + 'fue agregado correctamente')

def anadir_libro():
    titulo=input("Ingrese el titulo del libro: ")
    autor=input("Ingrese el nombre del autor: ")
    year=input("Ingrese el año de creacion: ")
    genero=input("Ingrese el genero: ")
    descripcion=input("Ingrese una breve descripcion del libro: ")

    objLibro=Libro(titulo,autor,year,genero,descripcion)
    lista_de_libros.append(objLibro)
    print("El libro" + titulo + "fue agregado correctamente. ")

def eliminar_libro():
    titulo = input("Ingrese el titulo del libro: ")
    for libro in lista_de_libros:
        if (libro.titulo == titulo):
            lista_de_libros.remove(libro)
            print('El libro ' + titulo + ' ha sido eliminado.')

def buscar_libro(propiedad_buscar):

    valor = input(f"Ingrese el valor de la propiedad {propiedad_buscar} del libro: ")
    for libro in lista_de_libros:
        if (getattr(libro,propiedad_buscar)==valor):
            print(" ID: " + str(libro.id) + " \n Titulo: " + libro.titulo + "\n Autor: " + libro.autor
                  + "\n Genero: " + libro.genero + "\n Descripcion: " + libro.descripcion + "\n Año: " + libro.year)

def modificar_atributos_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    year = input("Ingrese el año de creacion: ")
    genero = input("Ingrese el genero: ")
    descripcion = input("Ingrese una breve descripcion del libro: ")

    for libro in lista_de_libros:
        if libro.titulo == titulo:
            if (autor != ""):
                libro.autor = autor
            if (year != ""):
                libro.year = year

def mostrar_lista_libros():
    for libro in lista_de_libros:
        print(" ID: "+ str(libro.id) + " \n Titulo: " + libro.titulo+ "\n Autor: "+ libro.autor
              + "\n Genero: "+ libro.genero + "\n Descripcion: "+ libro.descripcion+ "\n Año: "+ libro.year)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_ingreso()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
