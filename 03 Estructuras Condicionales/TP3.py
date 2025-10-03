#Ejercicio 1: solicitar la edad del usuario. Si es mayor de 18 años, mostrar el mensaje "Es mayor de edad".

edad = int(input("Por favor, ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2: solicitar su nota al usuario. Si es mayor o igual a 6, mostrar mensaje "Aprobado", caso contrario mostrar "Desaprobado".

nota = int(input("Por favor, ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3: solicitar al usuario un número. Si es par, imprimir "Ha ingresaso un número par", de lo contrario imprimir "Por favor, ingrese un número par"

numero = int(input("Por favor, ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4: solicitar la edad al usuario e imprimer por pantalla a qué categoría pertenece.

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Niño/a: menor de 12 años")
elif edad >= 12 and edad < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años")
else:
    print("Adulto/a: mayor o igual que 30 años")

#Ejercicio 5: pedir al usuario ingresar constraseñas entre 8 y 14 caracteres (incluyendo 8 y 14).

contrasenia = input("Por favor, ingrese la contraseña: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6: calcular la moda, mediana y media de numeros aleatorios para determinar si hay sesgo positivo, negativo o no hay sesgo e imprimirlo por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

print(numeros_aleatorios)

mean_aleatorios = mean(numeros_aleatorios)
median_aleatorios = median(numeros_aleatorios)
mode_aleatorios = mode(numeros_aleatorios)

if mean_aleatorios > median_aleatorios and median_aleatorios > mode_aleatorios:
    print("Sesgo positivo o a la derecha")
elif mean_aleatorios < median_aleatorios and median_aleatorios < mode_aleatorios:
    print("Sesgo negativo o a la izquierda")
elif mean_aleatorios == median_aleatorios == mode_aleatorios:
    print("Sin sesgo")
else:
    print("No es distribución normal")

#Ejercicio 7: solicitar una frase o palabra al usuaraio. Si el string termina en vocal, añadir el signo de exlamación al final e imprimir el string.

#Ejercicio 8: solicitar al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee.

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 si desea su nombre en mayúsculas \nIngrese 2 si desea su nombre en minúsculas \nIngrese 3 si quiere su nombre con la primera letra mayúscula: "))

if opcion == 1:
    nombre_mayus = nombre.upper()
    print(f"Su nombre en mayúsculas es: {nombre_mayus}")
elif opcion == 2:
    nombre_minus = nombre.lower()
    print(f"Su nombre en minúsculas es: {nombre_minus}")
elif opcion == 3:
    nombre_letra = nombre.title()
    print(f"Su nombre con la primera letra en mayúscula es: {nombre_letra}")
else:
    print("Ingrese una opción válida.")

#Ejercicio 9: pedir al usuario la magnitud de un terremoto y clasificarla en una categoría según la escala de Richter.

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Escala de Ritcher: Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Escala de Ritcher: Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Escala de Ritcher: Moderado (sentido por personas, pero generalmente no causa daños.)")
elif magnitud >= 5 and magnitud < 6:
    print("Escala de Ritcher: Fuerte (puede causar daños en estructuras débiles.)")
elif magnitud >= 6 and magnitud < 7:
    print("Escala de Ritcher: Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Escala de Ritcher: Extremo (puede causar graves daños a gran escala)")
else:
    print("Por favor, ingrese un valor válido.")

#Ejercicio 10: preguntar al usuario en cuál hemisferio se encuentra, qué mes del año es y qué día es. Imprimir estación del año.

hemisferio = input("Presione N para hemisferio norte o S para hemisferio S: ")

if hemisferio == "N" or hemisferio == "n":
    mes = input("Ingrese el mes actual: ")
    mes_minus = mes.lower()
    if mes == "diciembre":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia < 21:
            print("La estación en el hemisferio norte actual es: Otoño")        
        elif dia >= 21 and dia <=31:
            print("La estación en el hemisferio norte actual es: Invierno")
        else:
            print("Ingrese un día válido")
    elif mes == "enero" or mes == "febrero":
        print("La estación en el hemisferio norte actual es: Invierno")
    elif mes == "marzo":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia <= 20:
            print("La estación en el hemisferio norte actual es: Invierno")
        elif dia > 20 and dia <= 31:
            print("La estación en el hemisferio norte actual es: Primavera")
        else:
            print("Ingrese un día válido")
    elif mes == "abril" or mes == "mayo":
        print("La estación en el hemisferio norte actual es: Primavera")
    elif mes == "junio":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia < 21:
            print("La estación en el hemisferio norte actual es: Primavera") 
        elif dia >= 21 and dia <= 30:
            print("La estación en el hemisferio norte actual es: Verano")
        else:
            print("Ingrese un día válido.")
    elif mes == "julio" or mes == "agosto":
        print("La estación en el hemisferio norte actual es: Verano")
    elif mes == "septiembre":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia <= 20:
            print("La estación en el hemisferio norte actual es: Verano")
        elif dia > 20 and dia <= 30:
            print("La estación en el hemisferio norte actual es: Otoño")
        else:
            print("Ingrese un día válido")
    elif mes == "octubre" or mes == "noviembre":
        print("La estación en el hemisferio norte actual es: Otoño")
    else:
        print("ingrese un mes válido")
elif hemisferio == "S" or hemisferio == "s":
    mes = input("Ingrese el mes actual: ")
    mes_minus = mes.lower()
    if mes == "diciembre":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia < 21:
            print("La estación en el hemisferio norte actual es: Primavera")        
        elif dia >= 21 and dia <=31:
            print("La estación en el hemisferio norte actual es: Verano")
        else:
            print("Ingrese un día válido")
    elif mes == "enero" or mes == "febrero":
        print("La estación en el hemisferio norte actual es: Verano")
    elif mes == "marzo":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia <= 20:
            print("La estación en el hemisferio norte actual es: Verano")
        elif dia > 20 and dia <= 31:
            print("La estación en el hemisferio norte actual es: Otoño")
        else:
            print("Ingrese un día válido")
    elif mes == "abril" or mes == "mayo":
        print("La estación en el hemisferio norte actual es: Otoño")
    elif mes == "junio":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia < 21:
            print("La estación en el hemisferio norte actual es: Otoño") 
        elif dia >= 21 and dia <= 30:
            print("La estación en el hemisferio norte actual es: Invierno")
        else:
            print("Ingrese un día válido.")
    elif mes == "julio" or mes == "agosto":
        print("La estación en el hemisferio norte actual es: Invierno")
    elif mes == "septiembre":
        dia = int(input("Ingrese el día actual: "))
        if dia >= 1 and dia <= 20:
            print("La estación en el hemisferio norte actual es: Invierno")
        elif dia > 20 and dia <= 30:
            print("La estación en el hemisferio norte actual es: Primavera")
        else:
            print("Ingrese un día válido")
    elif mes == "octubre" or mes == "noviembre":
        print("La estación en el hemisferio norte actual es: Primavera")
    else:
        print("ingrese un mes válido")
else: 
    print("Ingrese una opción válida.")