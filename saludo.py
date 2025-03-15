# ++++ 
from cliente import cliente

class saludo:
    def _init_(self):
        self.obj_cliente = cliente()
        
    def hacer_saludo_formal(self):
        mensaje = "saludo formal :"
        return mensaje 
    
    def hacer_despedida_formal(self):
        mensaje ="despedida formal: "
        return mensaje   