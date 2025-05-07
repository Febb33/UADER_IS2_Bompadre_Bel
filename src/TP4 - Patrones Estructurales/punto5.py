
class CharacterFlyweight:
    def __init__(self, char, font, size):
        self.char = char
        self.font = font
        self.size = size

    def render(self, position_x, position_y, color):
        print(f"Render '{self.char}' at ({position_x},{position_y}) "
              f"with font='{self.font}', size={self.size}, color={color}")


class CharacterFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, char, font, size):
        key = (char, font, size)
        if key not in cls._flyweights:
            cls._flyweights[key] = CharacterFlyweight(char, font, size)
        return cls._flyweights[key]


    def __init__(self):
        self.characters = []

    def add_character(self, char, font, size, x, y, color):
        flyweight = CharacterFactory.get_flyweight(char, font, size)
        self.characters.append((flyweight, x, y, color))

    def render(self):
        for flyweight, x, y, color in self.characters:
            flyweight.render(x, y, color)


doc = Document()
doc.add_character('H', 'Arial', 12, 0, 0, 'black')
doc.add_character('e', 'Arial', 12, 10, 0, 'black')
doc.add_character('l', 'Arial', 12, 20, 0, 'black')
doc.add_character('l', 'Arial', 12, 30, 0, 'black')
doc.add_character('o', 'Arial', 12, 40, 0, 'black')

doc.render()


print(f"Flyweights creados: {len(CharacterFactory._flyweights)}")
