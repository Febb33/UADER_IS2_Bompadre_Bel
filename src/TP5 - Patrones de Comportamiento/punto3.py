
class EmisorIDs:
    def __init__(self):
        self.observers = []

    def registrar(self, observer):
        self.observers.append(observer)

    def emitir_id(self, id_emitido):
        print(f"\n[Emisor] Emitiendo ID: {id_emitido}")
        for obs in self.observers:
            obs.notificar(id_emitido)


class ObservadorID:
    def __init__(self, id_propio):
        self.id_propio = id_propio

    def notificar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"✓ Observador con ID '{self.id_propio}' recibió su ID y responde.")
        else:
            print(f"- Observador con ID '{self.id_propio}' ignora el ID emitido.")


class ObservadorA(ObservadorID): pass
class ObservadorB(ObservadorID): pass
class ObservadorC(ObservadorID): pass
class ObservadorD(ObservadorID): pass


if __name__ == "__main__":

    emisor = EmisorIDs()

    obs1 = ObservadorA("AB12")
    obs2 = ObservadorB("CD34")
    obs3 = ObservadorC("EF56")
    obs4 = ObservadorD("GH78")

    emisor.registrar(obs1)
    emisor.registrar(obs2)
    emisor.registrar(obs3)
    emisor.registrar(obs4)

    ids_a_emitir = ["ZZ99", "AB12", "CD34", "XX00", "EF56", "GH78", "TT77", "AA11"]

    for id_ in ids_a_emitir:
        emisor.emitir_id(id_)
