#CEIC Libros
#Tabla de estudiantes
#Desarrollado por Forward
#Responsable del módulo: Diego Peña, 15-11095
#Fecha de inicio: 21-10-19, 16:48 am, Hora de Venezuela
#Última modifcación: 22-10-19, entrelas 10:00am y las 14:00pm, Hora de Venezuela

#Detalles de la manera actual, no se permiten correos o tlfs nulos pero la base de datos si los permite
#Tampoco se permiten apellidos con apóstrofes, sorry Connan O'Brian

from Prompt import ErrorPrompt, InfoPrompt
import re

#####################################################
#               Validadores de Estudiante           #
#####################################################
def check_pattern(name, pattern, title, message):
    if pattern.match(name) is None:
        ErrorPrompt(title, message)
        return False
    else:
        return True

def check_carnet(carnet):
    pattern = re.compile(r"^[0-9]{2}\-[0-9]{5}$")
    return check_pattern(carnet, pattern, "Error de formato", "Formato de carnet inválido")

def check_name(name, firstOrLast):
    if firstOrLast == 1: #Estamos validando un nombre
        pattern = re.compile(r"[a-zA-ZñÑáÁéÉíÍóÓúÚ]+$")
        ubicacion = "Caracter inválido en el nombre"
    else: #Estamos validando un apellido
        pattern = re.compile(r"[a-zA-ZñÑáÁéÉíÍóÓúÚ][a-zA-ZñÑáÁéÉíÍóÓúÚ ]+$")
        ubicacion = "Caracter inválido en el apellido"
    return check_pattern(name, pattern, "Caracter inválido", ubicacion)

def check_CI(number):
    pattern = re.compile(r"^[0-9]{6,8}$") 
    #Si este sistema perdura hasta que las cédulas tengan más de 8 dígitos, cambiar el 8 por el 9
    #y por favor avisarm porque wow, no debió llegar tan lejos
    return check_pattern(number, pattern, "Error de formato", "Formato de cédula inválido")

def check_phone(number):
    pattern = re.compile(r"^[0-9]{10,11}$") 
    return check_pattern(number, pattern, "Error de formato", "Número de teléfono inválido")

def check_email(address):
    pattern = re.compile(r"[a-zA-Z0-9\-_\.]+@[a-zA-Z0-9\-_\.]+")
    return check_pattern(address, pattern, "Email inválido", "Dirección de correo inválida")

def checkDays(days):
    pattern = re.compile(r"^[0-9]{1,3}$")
    return check_pattern(days, pattern, "Número de días inválidos", "Número de días inválidos")

def checkBooks(bookNo):
    pattern = re.compile(r"^[0-9]{2}$")
    return check_pattern(bookNo, pattern, "Número de libros inválido", "Número de libros inválido")

def checkDebt(debt):
    pattern  = re.compile(r"\d+(\.\d+)?")
    return check_pattern(debt, pattern, "Deuda inválida", "La cifra de la deuda es inválida")

def verification_estudiantes(fields, checkUntil):
    correct = True
    for i in range(checkUntil):
        if i == 0:
            correct = check_carnet(fields[i])
        elif i == 1 or i == 2:
            correct = check_name(fields[i], i)
        elif i == 3:
            correct = check_CI(fields[i])
        elif i == 4:
            correct = check_phone(fields[i])
        elif i == 5:
            correct = check_email(fields[i])
        elif i == 6:
            correct = checkDays(fields[i])
        elif i == 7:
            correct = checkBooks(fields[i])
        else:
            correct = checkDebt(fields[i])

        if not correct:
            return False

    return True


#####################################################
#               Validadores de libros               #
#####################################################
def checkIdBook(number):
    pattern = re.compile(r"^[0-9]{3,4}$")
    return check_pattern(number, pattern, "Código inválido", "Ese código de libro no es válido")

def checkTitle(title):
    pattern = re.compile(r"[a-zA-Z0-9ñÑáÁéÉíÍóÓúÚ \.,]+$")
    return check_pattern(title, pattern, "Caracter inválido", "Caracter inválido en el título")

def checkAuthor(name):
    pattern = re.compile(r"[a-zA-ZñÑáÁéÉíÍóÓúÚ \.,]+$")
    return check_pattern(name, pattern, "Caracter inválido", "Caracter inválido en nombre de autores")

def checkISBN(ISBN):
    #pattern = re.compile(r"^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$")             # Revisar aqui si no funciona http://regexlib.com/Search.aspx?k=ISBN
    #return check_pattern(ISBN, pattern, "Error de formato", "Número ISBN inválido")
    return True

def checkQuantity(number):
    pattern = re.compile(r"^[0-9]+$")                                                # Checkea si es un numero
    return check_pattern(number, pattern, "Error de formato", "Cantidad de libros inválida")

def checkQuantityLent(number):
    pattern = re.compile(r"^[0-9]+$")                                                # Checkea si es un numero
    return check_pattern(number, pattern, "Error de formato", "Cantidad de libros prestados inválida")

def checkLoanDuration(number):
    pattern = re.compile(r"^[0-9]+$")                                                # Checkea si es un numero
    return check_pattern(number, pattern, "Error de formato", "Número de dias inválido")

def verification_books(fields, checkUntil):
    correct = True
    for i in range(checkUntil):
        if i == 0:
            correct = checkIdBook(fields[i])
        elif i == 1:
            correct = checkTitle(fields[i])
        elif i == 2:
            correct = checkAuthor(fields[i])
        elif i == 3:
            correct = checkISBN(fields[i])
        elif i == 4:
            correct = checkQuantity(fields[i])
        elif i == 5:
            correct = checkQuantityLent(fields[i])
        elif i == 6:
            correct = checkLoanDuration(fields[i])

        if not correct:
            return False

    return True


#####################################################
#               Validadores de Usuarios             #
#####################################################
# Funcion para verificar si la longitud del nombre de usuario es correcta
def checkUsername(username):
    if len(username) < 33:
        return True
    else:
        ErrorPrompt("Error", "Nombre de usuario inválido, verifique la longitud del mismo")
        return False


def checkPermisos(permisos):
    if permisos != "Usuario" and permisos != "Administrador":
        ErrorPrompt("Error", "Sólo existen dos roles, Usuario y Administrador")
        return False
    else:
        return True

# Funcion que realiza la verificacion de todos los campos de la informacion de usuario a modificar o agregar
def verification_users(fields, checkUntil):
    correct = True
    for i in range(checkUntil):
        if i == 0:
            correct = checkUsername(fields[i])
        elif i == 1 or i == 2:
            correct = check_name(fields[i], i)
        elif i == 3:
            correct = check_email(fields[i])
        elif i == 4:
            correct = checkPermisos(fields[i])

        if not correct:
            return False

    return True
