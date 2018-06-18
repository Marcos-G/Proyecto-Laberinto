class vertice:
  def __init__(self,clave):
      self.posicion = clave
      self.conectadoA = {}
  def __hash__(self):
    return hash((self.posicion.coorx,self.posicion.coory))
  def __eq__(self,other):
    if(type(self)==type(None) or type(other)==type(None)):
      return False
    return (self.posicion==other.posicion)
  def __ne__(self,other):
    if(type(self)==type(None) or type(other)==type(None)):
      return True
    return (self.posicion!=other.posicion)
  def obtenerPosicion(self):
    return self.posicion

  def __str__(self):
    return str(self.posicion) + ' conectado a: ' + str([str(x.posicion)+str(self.obtenerDistancia(x)) for x in self.conectadoA])

    # El método agregarVecino se utiliza para agregar una conexión desde este vértice a otro.
  def agregarVecino(self,vecino,camino=None):
    self.conectadoA[vecino] = camino
    # Devuelve todos los vértices de la lista de adyacencia, representados por la variable conectadoA.
  def obtenerConexiones(self):
    return self.conectadoA.keys()

    # El método obtenerPonderacion devuelve la ponderación de la arista de este vértice al vértice pasado como parámetro.
  def obtenerDistancia(self,vecino):
    return len(self.conectadoA[vecino])-1

  def obtenerCamino(self,vecino):
    return self.conectadoA[vecino]
