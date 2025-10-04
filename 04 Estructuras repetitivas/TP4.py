#Ejercicio 1: imprimir en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

contador = 0

while contador <= 100:
    print(f"{contador}")
    contador +=1

#Ejercicio 2: solicitar un número entero y determinar la cantidad de dígitos que contiene.

numero = int(input("Ingrese un número entero mayor a 1: "))

contador = 0

while numero > 0:
    numero = numero // 10
    contador += 1

print(f"El número ingresado tiene {contador} digitos.")

#Ejercicio 3: sumar todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

suma = 0

for numero in range(num1 + 1, num2):
    suma += numero

print(f"La suma de todos los números (excluidos {num1} y {num2} es: {suma})")

#Ejercicio 4: ingresar números enteros y sumarlos en secuencia. Mostrar el total acumulado cuando el usuario ingrese un cero

total = 0
numero = 1

while numero !=0:
    numero = int(input("Ingresa un número entero: "))
    if numero != 0:
        total += numero
        print(f"Total acumulado hasta ahora {total}")

#Ejercicio 5: adivinar un número aleatorioi entre 0 y 9. Mostrar la cantidad de intentos para acertar.

import random 
numero_aleatorio = random.randint(0, 9)

numero_ingresado = int(input("¿En qué número estoy pensando?: "))

contador = 0

while numero_ingresado != numero_aleatorio:
    contador += 1
    numero_ingresado = int(input("No exactamente. Inténtalo de nuevo: "))

print(f"Estaba pensando en el número {numero_aleatorio}. Lograste adivinarlo en {contador} intentos.")

#Ejercicio 6: imprimir en pantalla todos los números pares comprendidos entre 0 y 100 en orden decreciente.

for num in range(100, -1, -2):
    print(num)

#Ejercicio 7: calcular la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingresa un número entero: "))

suma = 0

for i in range(0, numero + 1):
    suma += i

print(f"La suma de todos los números comprendidos entre 0 y {numero} es: {suma}.")

#Ejercicio 8: ingresar 100 números enteros, indicar cuántos de estos son pares, cuántos impares, cuántos negativos y cuántos negativos.

ingreso = 1
par = 0
impar = 0
negativo = 0
positivo = 0

while ingreso <= 100:
    numero = int(input("Ingresa un número entero: "))
    ingreso += 1
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    if numero >= 0:
        positivo += 1
    else:
        negativo += 1

print(f"De los números ingresados, {par} son pares, {impar} son impares, {negativo} son negativos y {positivo} son positivos.")
    
#Ejercicio 9: ingresar 100 números enteros y calcular la media de esos valores.

from statistics import mean

numeros = []
ingreso = 1

while ingreso <= 100:
    numero = int(input("Ingresa un número entero: "))
    numeros.append(numero)
    ingreso += 1

media = mean(numeros)

print(f"La media de los números ingresados es: {media}")

#Ejercicio 10: invertir el orden de los dígitos de un número ingresado por el usuario.

