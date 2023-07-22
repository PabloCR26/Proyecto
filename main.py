from usuario import Usuario

lista_de_usuarios=[]

def menu_ingreso():

    while True:
        opcion = int(input(' Menu\n----------\t'+
                       '\n\t1. Añadir nuevo libro'
                       '\n\t2. Ver lista de libros'
                       '\n\t3. Buscar libro por título'
                       '\n\t4. Inscribir usuario'
                       '\n\t5. Inscribir empleado'
                       '\n\t6. Eliminar libros'
                       '\n\t7. Reservar libro'
                       '\n\t8. Filtrar libros'
                       '\n\t9. Modificar atributos del libro'
                       '\n\t10. Prestamo de libro'
                       '\n\t11. Devolución de libro'
                       '\n\t12. Generar informe'
                       '\n\t13. Salir del sistema'
                       '\nIngrese la opcion que desea:\n'))

        if opcion ==1:
            print('Añadiendo el nuevo libro')
        elif opcion ==2:
            print('Mostrando la lista de libros')
        elif opcion ==3:
            print('Buscando el libro por título')
        elif opcion ==4:
            crear_usuario()
            print('Usuario inscrito')
        elif opcion ==5:
            print('Empleado instrito')
        elif opcion ==6:
            print('Libro eliminado')
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_ingreso()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
