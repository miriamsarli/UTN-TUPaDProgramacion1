#Ejercicio 1: Crear una lista con las notas de 10 estudiantes. Mostrar lista, calcular y mostrar promedio, indicar nota más alta y más baja

from statistics import mean

notas = [5,10,8,8,6,4,7,7,9,5]

promedio = mean(notas)
print(f"El promedio es {promedio}")
nota_min= min(notas)
nota_max= max(notas)
print(f"La nota más alta es {nota_max} y la nota más baja {nota_min}")

#Ejercicio 2: Pedir al usuario que cargue 5 productos en una lista. Mostrarla ordenada alfabéticacmente

lista_productos = []
carga = 1

while carga <= 5:
    producto = input("Ingrese un producto: ")
    lista_productos.append(producto)
    carga +=1

lista_ordenada = sorted(lista_productos)
print(f"Los productos ingresados son: {lista_ordenada}")

eliminar_producto = input("Ingrese el producto a eliminar: ")
lista_ordenada.remove(eliminar_producto)
print(f"Los productos solicitados son: {lista_ordenada}")

#Ejercicio 3: Generar una lista con 15 números enteros al azar entre 1 y 100. Crear lista con los pares y otra con los impares. 


#Ejercicio 4: Dada una lista con valores repetidos, crear una nueva lista sin elementos repetidos.

#Ejercicio 5: Crear una lista con los nombres de 8 estudiantes presente en clase.

#Ejercicio 6: dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha

#Ejercicio 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana

#Ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias.

#Ejercicio 9: Representar un tablero de Ta-Te-Ti como una lista de listas 3x3

#Ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7