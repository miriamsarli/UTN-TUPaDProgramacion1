#Actividad 1: crear un programa que imprima por pantalla el mensaje: "Hola Mundo!"

print("Hola Mundo!")

#Actividad 2: pedir al usuario su nombre e imprimir por pantalla un saludo usándolo.

nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola, {nombre}!")

#Actividad 3: pedir al usuario, nombre, apellido, edad y lugar de residencia e imprimirlo en una oración.

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Ingrese ahora su edad: "))
residencia = input("Ingrese en qué provincia reside: ")

print(f"Soy {nombre}{apellido}, tengo {edad} y vivo en {residencia}.")

#Actividad 4: pedir al usuario el radio de un círculo e imprimir por pantalla su área y su perímetro

radio = int(input("Por favor, ingrese el radio del círculo en metros: "))

area = 3.1416 * (radio ** 2)
perimetro = 2 * 3.1416 * radio

print(f"El área del círculo es {area} metros cuadrados y su perímetro {perimetro} metros.")

#Actividad 5: pedir al usuario una cantidad de segundos e imprimir por pantalla a cuántas horas equivale.

segundos = int(input("Por favor, ingresa la cantidad de segundos: "))

horas = (segundos/60)/60

print(f"{segundos} segundos equivalen a {horas} horas.")

#Actividad 6: pedir al usuario un número e imprimir por pantalla la tabla de multiplicar de dicho número.

#Actividad 7: pedir al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos multiplicarlos y restarlos.

numero1 = int(input("Por favor, ingresa un número distinto de cero: "))
numero2 = int(input("Por favor, ingresa otro número distinto de cero: "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"El resultado de sumar {numero1} y {numero2} es {suma}")
print(f"El resultado de dividir {numero1} y {numero2} es {division}")
print(f"El resultado de multiplicar {numero1} y {numero2} es {multiplicacion}")
print(f"El resultado de resta {numero1} y {numero2} es {resta}")

#Actividad 8: pedir al usuario su altura y peso e imprimir por pantalla su índice de masa corporal.

altura = float(input("Por favor, ingresa tu altura: "))
peso = float(input("Por favor, ingresa tu peso: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal es de {imc}")

#Actividad 9: pedir al usuario una temperatura en grados Celsius e imprimir por pantalla su equivalente en grados Fahrenheit.

gradosCelsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))

gradosFahrenheit = ((gradosCelsius * 9)/5) + 32

print(f"La temperatura en grados Fahrenheit es de {gradosFahrenheit}")

#Actividad 10: pedir al usuario 3 números e imprimir por pantalla el promedio de dichos números.

num1 = int(input("Por favor, ingresa un número entero: "))
num2 = int(input("Por favor, ingresa otro número entero: "))
num3 = int(input("Por favor, ingresa un último número entero: "))

promedio = (num1 + num2 + num3)/ 3

print(f"El promedio de los 3 números ingresados es {promedio}")