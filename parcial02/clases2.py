"""Crear una clase `Rectangulo` que tenga los atributos `ancho` y
`alto`. Además, debe tener dos métodos: `area` que calcule el área
del rectángulo, y `perimetro` que calcule el perímetro.
"""

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

#Se prueba la clase
rectangulo1 = Rectangulo(4, 7)
print(rectangulo1.area())        # Salida: 28
print(rectangulo1.perimetro())   # Salida: 22
