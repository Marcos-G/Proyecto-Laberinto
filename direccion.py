from enum import Enum   
Direccion = Enum('Direccion', 'arriba derecha abajo izquierda')
def invDir(dire):
  if(dire==Direccion.arriba):
    return Direccion.abajo
  elif(dire==Direccion.abajo):
    return Direccion.arriba
  elif(dire==Direccion.derecha):
    return Direccion.izquierda
  elif(dire==Direccion.izquierda):
    return Direccion.derecha