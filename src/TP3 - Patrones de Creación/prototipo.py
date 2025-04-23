
import copy

class Prototipo:
    def __init__(self, nombre, atributos=None):
        self.nombre = nombre
        self.atributos = atributos if atributos else {}

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar_info(self):
        print(f"Soy una instancia de: {self.nombre}")
        print(f"Atributos: {self.atributos}")
