import libro
from libro import Libro
from usuario import Usuario
from empleado import Empleado
from colorama import Fore
import openpyxl
from fpdf import FPDF

lista_de_usuarios = []
lista_de_empleados = []
lista_de_libros = []
libros_prestados =dict()


def menu_ingreso():
    while True:
        opcion = int(input(' Menu\n----------\t' +
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

        if opcion == 1:
            anadir_libro()
        elif opcion == 2:
            mostrar_lista_libros()
        elif opcion == 3:
            buscar_libro("titulo")
        elif opcion == 4:
            buscar_libro("id")
        elif opcion == 5:
            buscar_libro("autor")
        elif opcion == 6:
            buscar_libro("year")
        elif opcion == 7:
            buscar_libro("genero")
        elif opcion == 8:
            crear_usuario()
        elif opcion == 9 :
            cargar_empleados()
        elif opcion == 10:
            eliminar_libro()
        elif opcion == 11:
            reservar()
        elif opcion == 12:
            filtrar_libros_genero()
        elif opcion == 13:
            modificar_atributos_libro()
        elif opcion == 14:
            prestamo_libro()
        elif opcion == 15:
            devolucion_libro()
        elif opcion == 16:
            generar_informes()
        elif opcion == 17:
            break
        else:
            print('¡Opción no valida!')


def crear_usuario():
    cedula = input("Ingrese su numero de cedula: ")
    nombre = input("Ingrese su nombre: ")
    apellido1 = input("Ingrese su primer apellido: ")
    apellido2 = input("Ingrese su segundo apellido: ")
    direccion = input("Ingrese su direccion: ")
    telefono = input("Ingrese su numero de telefono: ")

    objUsuario = Usuario(cedula, nombre, apellido1, apellido2, direccion, telefono)
    lista_de_usuarios.append(objUsuario)
    print("Usuario: " + nombre + " agregado correctamente.")


def cargar_empleados():
    with open('empleados.txt', 'r') as f:
        for linea in f:
            datos = linea.split(',')
            obj_empleado = Empleado(datos[0], datos[2], datos[3], datos[4], datos[1], datos[5])
            lista_de_empleados.append(obj_empleado)
            print('El empleado ' + obj_empleado.nombre + ' fue agregado correctamente')


def anadir_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    year = input("Ingrese el año de creacion: ")
    genero = input("Ingrese el genero: ")
    descripcion = input("Ingrese una breve descripcion del libro: ")

    objLibro = Libro(titulo, autor, year, genero, descripcion)
    lista_de_libros.append(objLibro)

    print("El libro " + titulo + " con el ID " + str(objLibro.id) + " fue agregado correctamente. ")


def eliminar_libro():
    id = input("Ingrese el ID del libro: ")
    for libro in lista_de_libros:
        if (str(libro.id) == id):
            lista_de_libros.remove(libro)
            print('El libro ' + id + ' ha sido eliminado.')


def buscar_libro(propiedad_buscar):
    valor = input(f"Ingrese el valor de la propiedad {propiedad_buscar} del libro: ")
    for libro in lista_de_libros:
        if (str(getattr(libro, propiedad_buscar)) == valor):
            print(" ID: " + str(libro.id) + " \n Titulo: " + libro.titulo + "\n Autor: " + libro.autor
                  + "\n Genero: " + libro.genero + "\n Descripcion: " + libro.descripcion + "\n Año: " + libro.year)

def filtrar_libros_genero():
    valor = input('Ingrese el género del libro a filtrar: ')
    libros_filtrados = list(filter(lambda libro: libro.genero == valor,lista_de_libros))
    print('Los libros que coinciden son: ')
    for libros in libros_filtrados:
        print(libros.titulo)


def modificar_atributos_libro():
    id = input("Ingrese el ID del libro: ")
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    year = input("Ingrese el año de creacion: ")
    genero = input("Ingrese el genero: ")
    descripcion = input("Ingrese una breve descripcion del libro: ")

    for libro in lista_de_libros:
        if str(libro.id) == id:
            if (titulo != ""):
                libro.titulo = titulo
            if (autor != ""):
                libro.autor = autor
            if (year != ""):
                libro.year = year
            if (genero != ""):
                libro.genero = genero
            if (descripcion != ""):
                libro.descripcion = descripcion
            print(" Los atributos han sido modificados!!! ")


def mostrar_lista_libros():
    for libro in lista_de_libros:
        print(" ID: " + str(libro.id) + " \n Titulo: " + libro.titulo + "\n Autor: " + libro.autor
              + "\n Genero: " + libro.genero + "\n Descripcion: " + libro.descripcion + "\n Año: " + libro.year)


def prestamo_libro():
    id = input("Ingrese el ID del libro que desea solicitar: ")
    cedula = input("Ingrese la cédula del usuario: ")
    fecha_prestamo = input("Ingrese fecha de inicio de prestamo del libro: ")
    fecha_devolucion = input("Ingrese fecha de devolucion del libro: ")
    for libro in lista_de_libros:
        if str(libro.id) == id:
            if libro.disponible:
                libro.prestar(fecha_prestamo, fecha_devolucion)
                datos = libros_prestados.get(cedula)
                libros_usuarios = datos["libros"]
                if (libros_usuarios):
                    libros_usuarios.append(libro)
                    libros_prestados.update(cedula, { "¨libros":libros_prestados})
                else:
                    libros_prestados[cedula] = {"¨libros": [libro]}
                print("Dic: ", libros_prestados.items())
                print("Su libro ha sido prestado correctamente")
            else:
                print("Su libro no se encuentra disponible!!")

def reservar():
    id = input("Ingrese el ID del libro que desea reservar : ")
    fecha_inicio = input('Ingrese la fecha de inicio de la reserva: ')
    fecha_final = input('Ingrese la fecha de fin de la reserva: ')
    for libro in lista_de_libros:
        if str(libro.id) == id:
            if not libro.reservado:
                libro.reservar(fecha_inicio, fecha_final)
                print('Su libro se ha reservado correctamente. ')
            else:
                print("Su libro no se encuentra disponible!")


def devolucion_libro():
    id = input("Ingrese el ID del libro que desea devolver : ")
    for libro in lista_de_libros:
        if str(libro.id) == id:
            if not libro.disponible:
                libro.devolver()
            else:
                print("Su libro no se encuentra disponible!!")


def generar_informes():
    opcion_informe = int(input("1. Libros disponibles en la biblioteca\n"
                               "2. Inventario total\n"
                               "3. Prestamos vigentes\n"
                               "4. Usuarios registrados\n"
                               "Ingrese lo que desea generar:\n"))
    if opcion_informe == 1:
        libros_disponibles()
    elif opcion_informe == 2:
        inventario_total()
    elif opcion_informe == 3:
        libros_prestados()
    elif opcion_informe == 4:
        usuarios_registrados()
    else:
        print("Ingrese una opcion valida!!")


def libros_disponibles():
    libros_disponibles=[]
    for libro in lista_de_libros:
        if libro.disponible:
            libros_disponibles.append(libro)
    formato_generar(libros_disponibles)

def libros_prestados():
    libros_prestados=[]
    for libro in lista_de_libros:
        if not libro.disponible:
            libros_prestados.append(libro)
    formato_generar(libros_prestados)

def inventario_total():
    formato_generar(lista_de_libros)

def usuarios_registrados():
    formato_generar(lista_de_usuarios)



def formato_generar(datos):
    opcion = int(input('Seleccione e el formato del archivo para guardar:\n'
                       '1. Archivo de texto\n'
                       '2. Archivo PDF \n'
                       '3. Archivo de Excel \n'
                       'Ingrese su opcion:'))

    if opcion == 1:
        generar_txt(datos)
    elif opcion == 2:
        generar_pdf(datos)
    elif opcion == 3:
        generar_excel(datos)
    else:
        print("Ingrese una opcion valida!!")

def generar_txt(datos_guardar):
    nombre_archivo = input('Ingrese el nombre del archivo:')
    with open(nombre_archivo + '.txt', 'w') as f:
        for linea in datos_guardar:
            f.write(linea.__str__())
        print(Fore.RED + 'El archivo se guardó correctamente' + Fore.RESET)
def generar_pdf(datos_guardar):
    nombre_archivo = input('Ingrese el nombre del archivo: ')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    for nombre in (datos_guardar):
        pdf.cell(0, 5, txt=nombre.__str__(), ln=True)
    pdf.output(nombre_archivo + '.pdf')
    print(Fore.RED + 'El archivo se guardó correctamente' + Fore.RESET)

def generar_excel(datos_guardar):
    nombre_archivo = input("Ingrese el nombre del archivo")
    libro = openpyxl.Workbook()
    hoja = libro.active

    for i, nombre in enumerate(datos_guardar, start=1):
        hoja.cell(row=i, column=1, value=nombre.__str__())
    libro.save(nombre_archivo + ".xlsx")
    print(Fore.RED + 'El archivo se guardó correctamente' + Fore.RESET)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_ingreso()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
