"""a. Escribir un programa que muestre los números del 1 al 10
utilizando un bucle for.
b. Escribir un programa que muestre la suma de los números del
1 al 100.
"""

#Desarrollo a.
print ("Se muestran los numeros del 1 al 10")
for i in range (11):
    print(i)

#Desarrollo b.
print ("Ahora se muestra la suma de los numeros del 1 al 100:")
#Inicio la variable para almacenar la suma
suma = 0 
for numero in range (1, 101):
    suma += numero

    print("La suma de los numeros del 1 al 100 es: ", suma)