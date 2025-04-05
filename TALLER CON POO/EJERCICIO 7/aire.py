class AireAcondicionado:
    def __init__(self):
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("Aire acondicionado encendido.")

    def apagar(self):
        self.encendido = False
        print("Aire acondicionado apagado.")

    def estado(self):
        return "Encendido" if self.encendido else "Apagado"