
class Hamburguesa:
    def __init__(self, nombre="Hamburguesa"):
        self.nombre = nombre

    def entregar_en_mostrador(self):
        print(f"{self.nombre} entregada en mostrador.")

    def retirada_por_cliente(self):
        print(f"{self.nombre} retirada por el cliente.")

    def enviar_por_delivery(self):
        print(f"{self.nombre} enviada por delivery.")
