from suds.client import Client
import json
import emoji


url = "http://localhost:7777/ws/AcademicoWebService?wsdl"
client = Client(url)
service = client.service
# Prefixes (1)
#       ns0 = "http://soap.sparkjavasoap.avathartech.com/"
#    Ports (1):
#       (AcademicoWebServicePort)
#          Methods (5):
#             getAllEstudiante()
#             getAsignatura(xs:int arg0, )
#             getEstudiante(xs:int arg0, )
#             getProfesor(xs:string arg0, )
#             holaMundo(xs:string arg0, )
#          Types (13):
#             asignatura
#             estudiante
#             getAllEstudiante
#             getAllEstudianteResponse
#             getAsignatura
#             getAsignaturaResponse
#             getEstudiante
#             getEstudianteResponse
#             getProfesor
#             getProfesorResponse
#             holaMundo
#             holaMundoResponse
#             profesor


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


class Estudiante:
    def __init__(self, nombre, matricula=None):
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        estudiante = "Nombre: " + str(self.nombre) + "\nMatricula: " + str(
            self.matricula)
        return estudiante


class Profesor:
    def __init__(self, nombre, cedula=None):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        profesor = "Nombre: " + str(self.nombre) + "\nCedula: " + str(
            self.cedula)
        return profesor


class Asignatura:
    def __init__(self, nombre, clave=None):
        self.nombre = nombre
        self.clave = clave

    def __str__(self):
        asignatura = "Nombre: " + str(self.nombre) + "\nClave: " + str(
            self.clave)
        return asignatura


def print_menu():
    print()
    print("-------------------- SOAP     Api " +
          emoji.emojize(":grinning_face_with_big_eyes:") + "  ----------------------")
    print("| Eliga la opción deseada en las siguientes opciones: |")
    print("| 1. Lista de Estudiantes                             |")
    print("| 2. Información de Estudiante                        |")
    print("| 3. Información de Profesor                          |")
    print("| 4. Información de Asignatura                        |")
    print("| 0. Exit                                             |")
    print("-------------------------------------------------------")


def get_estudiantes():
    req = service.getAllEstudiante()
    lista_estudiantes = []
    for est in req:
        estudiante = Estudiante(est.nombre, est.matricula)
        lista_estudiantes.append(estudiante)
        print(estudiante)
    print()


def get_profesor():
    cedula = input("Inserte la cedula del profesor: ")
    prof = service.getProfesor(cedula)
    profesor = Profesor(prof.nombre, prof.cedula)
    print("\n" + str(profesor))
    return profesor


def get_estudiante():
    matricula = int(input("Inserte la matricula del estudiante: "))
    est = service.getEstudiante(matricula)
    estudiante = Estudiante(est.nombre, est.matricula)
    print("\n" + str(estudiante))
    return estudiante


def get_asignatura():
    id_asignatura = int(input("Inserte el ID de la asignatura: "))
    asg = service.getAsignatura(id_asignatura)
    asignatura = Asignatura(asg.nombre, asg.clave)
    print("\n" + str(asignatura))
    return asignatura


opcion = -1
while True:
    print_menu()
    opcion = int(input("Opción tomada: "))

    if opcion == 0:
        break
    elif opcion == 1:
        get_estudiantes()
    elif opcion == 2:
        get_estudiante()
    elif opcion == 3:
        get_profesor()
    elif opcion == 4:
        get_asignatura()
