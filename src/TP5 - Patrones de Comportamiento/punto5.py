
import os

class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	def __init__(self):
		self.history = []

	def save(self, writer):
		if len(self.history) == 4:
			self.history.pop(0)
		self.history.append(writer.save())

	def undo(self, writer, index=0):
		if 0 <= index < len(self.history):
			writer.undo(self.history[-(index+1)])
		else:
			print(f"No hay un estado guardado en la posición {index}.")


if __name__ == '__main__':
	os.system("clear")
	print("Crea un objeto que gestionará versiones anteriores")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional y se salva")
	writer.write("Material adicional 1\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional 2 y se salva")
	writer.write("Material adicional 2\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional 3 y se salva")
	writer.write("Material adicional 3\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional 4 (no se salva para ver el efecto del undo)")
	writer.write("Material adicional 4 (no guardado)\n")
	print(writer.content + "\n")

	print("Se invoca a <undo(0)>")
	caretaker.undo(writer, 0)
	print("Estado actual:\n" + writer.content + "\n")

	print("Se invoca a <undo(1)>")
	caretaker.undo(writer, 1)
	print("Estado actual:\n" + writer.content + "\n")

	print("Se invoca a <undo(3)> (el más antiguo)")
	caretaker.undo(writer, 3)
	print("Estado actual:\n" + writer.content + "\n")

	print("Se invoca a <undo(4)> (inexistente)")
	caretaker.undo(writer, 4)
