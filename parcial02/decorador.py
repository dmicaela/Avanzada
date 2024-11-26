"""Crear un decorador con el nombre “decorador_mensaje” que
imprima un mensaje antes y después de la ejecución de la función
decorada.
Crear una función con el nombre “funcion_principal” que
imprima en pantalla el texto: “Esta es la función principal”.
Decorar esta funcion con el decorador y luego ejecutarla."""

# Se define el decorador_mensaje
def decorador_mensaje(func):
    def wrapper():
        print("Inicio de la funcion.")
        func()
        print("Fin de la funcion.")
    return wrapper

# Función principal decorada
@decorador_mensaje
def funcion_principal():
    print("Esta es la funcion principal.")

# Llamada a la función decorada
funcion_principal()
