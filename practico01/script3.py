"""Crear un script con una lista mi_lista que contenga tres tipos
diferentes de datos."""
print("Contenido de mi lista inicial")
mi_lista = [150, "Hola, soy Mica", 5.90]
print (mi_lista)
"""Agregar un nuevo elemento al final de la lista con el método 
append()."""
mi_lista.append(False)
print("Un elemento nuevo se agrego al final: ", mi_lista)
"""Cambiar el valor del primer elemento de la lista. """
mi_lista[0] = "Terrazas"
print ("Se cambia el valor del primer elemento: ", mi_lista)
"""Eliminar el último elemento de la lista con el método pop()."""
mi_lista.pop()
print ("Se elimina el ultimo elemento de la lista", mi_lista)
"""Mostrar en pantalla el contenido de la lista."""
print("Contenido nuevo de mi lista:", mi_lista)
