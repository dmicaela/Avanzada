"""Escribir un programa que le solicite al usuario ingresar una
calificación del 0 al 100, la asigne a una variable y muestre la
calificación alfabética correspondiente (A, B, C, D, F) según el
numero ingresado. Correspondiendo cada letra con valores de 20 en
20. Es decir: 0 a 19 = A, de 20 a 39 = B, etc"""

numero = int(input("Ingresa una calificación del 0 al 100: "))
"""Verificamos que la calificacion entre en el rango valido"""
if numero < 0 or numero > 100:
    print("Por favor, la calificación debe estar entre 0 y 100.")
else:
    if numero < 20:
        letra = 'A'
    elif numero < 40:
        letra = 'B'
    elif numero < 60:
        letra = 'C'
    elif numero < 80:
        letra = 'D'
    else: 
        letra = 'E'

    print("La calificación alfabética es:", letra)
