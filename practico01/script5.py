"""Crear un script con un diccionario mi_diccionario con tres 
pares de clave:valor, de 3 tipos diferentes"""

mi_diccionario = {
    "nombre": "Micaela",
    "edad": 25,
    "altura": 1.55
}
print("Este es mi diccionario inicial: ", mi_diccionario)
"""Imprimir el valor de la primer clave."""
print("El valor de la primera clave 'nombre':", mi_diccionario["nombre"])
"""Añade un nuevo par clave:valor al diccionario."""
"""Intenta cambiar el valor de la segunda clave existente.
Imprimir el contenido del diccionario en pantalla."""
mi_diccionario["vivo en"] = "Patagones"
mi_diccionario["edad"] = 30

print("Este es el contenido de mi diccionario: ", mi_diccionario)