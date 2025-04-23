
class Boton:
    def dibujar(self): pass

class Checkbox:
    def dibujar(self): pass


class BotonWindows(Boton):
    def dibujar(self): print("Dibujando botón estilo Windows")

class CheckboxWindows(Checkbox):
    def dibujar(self): print("Dibujando checkbox estilo Windows")


class BotonMac(Boton):
    def dibujar(self): print("Dibujando botón estilo Mac")

class CheckboxMac(Checkbox):
    def dibujar(self): print("Dibujando checkbox estilo Mac")


class GUIFactory:
    def crear_boton(self): pass
    def crear_checkbox(self): pass


class WindowsFactory(GUIFactory):
    def crear_boton(self): return BotonWindows()
    def crear_checkbox(self): return CheckboxWindows()

class MacFactory(GUIFactory):
    def crear_boton(self): return BotonMac()
    def crear_checkbox(self): return CheckboxMac()
