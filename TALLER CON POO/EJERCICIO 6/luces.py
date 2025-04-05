class Luces:
    def __init__(self):
        self.encendidas = False

    def encender(self):
        self.encendidas = True
        print("Luces encendidas.")

    def apagar(self):
        self.encendidas = False
        print("Luces apagadas.")

    def estado(self):
        return "Encendidas" if self.encendidas else "Apagadas"