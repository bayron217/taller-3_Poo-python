class Alarma:
    def __init__(self):
        self.activada = False

    def activar(self):
        self.activada = True
        print("Alarma activada.")

    def desactivar(self):
        self.activada = False
        print("Alarma desactivada.")

    def estado(self):
        return "Activada" if self.activada else "Desactivada"