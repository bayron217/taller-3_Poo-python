class Sensores:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0

    def leer_temperatura(self):
        # Simulamos la lectura de temperatura (puedes cambiarla manualmente)
        self.temperatura = float(input("Ingrese la temperatura actual (°C): "))

    def leer_humedad(self):
        # Simulamos la lectura de humedad (puedes cambiarla manualmente)
        self.humedad = float(input("Ingrese la humedad actual (%): "))