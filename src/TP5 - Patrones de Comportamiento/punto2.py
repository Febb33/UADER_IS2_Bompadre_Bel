
class StringIterator:
    def __init__(self, data, reverse=False):
        self.data = data
        self.reverse = reverse
        self.index = len(data) - 1 if reverse else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.reverse:
            if self.index < 0:
                raise StopIteration
            char = self.data[self.index]
            self.index -= 1
        else:
            if self.index >= len(self.data):
                raise StopIteration
            char = self.data[self.index]
            self.index += 1
        return char


class CadenaIterable:
    def __init__(self, cadena):
        self.cadena = cadena

    def iterador_normal(self):
        return StringIterator(self.cadena, reverse=False)

    def iterador_reverso(self):
        return StringIterator(self.cadena, reverse=True)


if __name__ == "__main__":
    texto = CadenaIterable("UADER")

    print("Recorrido directo:")
    for c in texto.iterador_normal():
        print(c, end=" ")

    print("\n\nRecorrido reverso:")
    for c in texto.iterador_reverso():
        print(c, end=" ")
