
from abc import ABC, abstractmethod


class TrenLaminador(ABC):
    @abstractmethod
    def producir(self, lamina_id):
        pass


class Tren5m(TrenLaminador):
    def producir(self, lamina_id):
        print(f"Lámina {lamina_id}: producida en tren de 5 metros")


class Tren10m(TrenLaminador):
    def producir(self, lamina_id):
        print(f"Lámina {lamina_id}: producida en tren de 10 metros")


class Lamina:
    def __init__(self, id_lamina, tren: TrenLaminador):
        self.id = id_lamina
        self.tren = tren

    def producir(self):
        self.tren.producir(self.id)


if __name__ == "__main__":

    tren_corto = Tren5m()
    tren_largo = Tren10m()

    lamina1 = Lamina("A001", tren_corto)
    lamina2 = Lamina("A002", tren_largo)

    lamina1.producir()
    lamina2.producir()