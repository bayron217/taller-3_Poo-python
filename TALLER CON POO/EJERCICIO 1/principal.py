from cliente import cliente
from saludo import saludo
# +++++++codigo principal+++++++


#creando objetos
obj_cliente = cliente()
obj_saludo = saludo()
#llamo a los metodos del objeto
obj_cliente.tomar_datos()
aux_mensaje = obj_saludo.hacer_saludo_formal()
obj_cliente.hacer_saludo(aux_mensaje)