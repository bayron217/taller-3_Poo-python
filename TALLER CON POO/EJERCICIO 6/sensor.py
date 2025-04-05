class SensorMovimiento:
    def __init__(self):
        self.movimiento = False

    def detectar_movimiento(self):
        # Simulamos la detección de movimiento (puedes cambiarla manualmente)
        respuesta = input("¿Hay movimiento en la habitación? (s/n): ").lower()
        self.movimiento = respuesta == "s"