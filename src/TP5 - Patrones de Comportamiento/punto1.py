
class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        if self.next_handler:
            self.next_handler.handle(number)
        else:
            print(f"{number} no fue consumido.")


class ParHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} fue consumido por ParHandler")
        else:
            super().handle(number)


class PrimoHandler(Handler):
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.es_primo(number):
            print(f"{number} fue consumido por PrimoHandler")
        else:
            super().handle(number)


class NoConsumidoHandler(Handler):
    def handle(self, number):
        print(f"{number} no fue consumido por ningún handler.")


if __name__ == "__main__":

    handler = ParHandler(PrimoHandler(NoConsumidoHandler()))

    for i in range(1, 101):
        handler.handle(i)
