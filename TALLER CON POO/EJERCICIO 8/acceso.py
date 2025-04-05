class ControlAcceso:
    def __init__(self):
        self.horario_activo = True  # Simula si está dentro del horario de atención

    def verificar_acceso(self, cliente):
        if (cliente.tiene_membresia and self.horario_activo) or cliente.es_empleado:
            return "Acceso permitido."
        else:
            return "Acceso denegado."