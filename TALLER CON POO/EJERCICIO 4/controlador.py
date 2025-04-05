class ControladorInvernadero:
    def __init__(self):
        self.estado = "Inactivo"

    def controlar_temperatura(self, temperatura):
        if temperatura < 10:
            self.estado = "Calefactor activado"
        elif 10 <= temperatura <= 25:
            self.estado = "Inactivo"
        else:
            self.estado = "Ventilador activado"

    def obtener_estado(self):
        return self.estado