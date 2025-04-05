# ******** zona de clase ************
#se crea la clase
class cliente:
    #se crea el modelo constructor
    def __init__(self):
        #se crean atributos de clase
        self.nombre_cliente = " "
        self.apellido_cliente = " "



   #crear metodos get y set por atributos
    def get_nombre(self):
        return self.nombre_cliente

    def get_apellido(self):
        return self.apellido_cliente

    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre

    def set_apellido(self, dato_apellido):
        self.apellido_cliente = dato_apellido

   
   

    #se crean metodos normales de la clase
    def tomar_datos(self):
      self.nombre_cliente = input("Ingrese su nombre: ")
      self.apellido_cliente = input("Ingrese su apellido: ")
    
    def procesar_datos (self):
      aux = self.nombre_cliente + " " + self.apellido_cliente

    def mostrar_cliente(self):
      print(f"Nombre: {self.nombre_cliente}")
      print(f"Apellido: {self.apellido_cliente}")

    def hacer_saludo(self, datoSaludo):
       print(f"{datoSaludo} : {self.nombre_cliente}  {self.apellido_cliente}")
    
       

