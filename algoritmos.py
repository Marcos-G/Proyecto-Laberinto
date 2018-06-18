from tablero import *
from random import randint
from vertice import vertice


def crearLaberinto(tablero):
	size=tamaño(tablero)
	n=size**2
	c=0
	caminos=[]
	caminosf=[]
	entrada=coordenada(randint(0,size-1),0)
	tirarES(tablero,entrada,Direccion.arriba)
	caminos.append(entrada)
	caminosf.append(entrada)
	while(len(caminos)<n*1):
		c+=1
		nodo=caminosf[randint(0,len(caminosf)-1)]
		dire=dirAl()
		nextNodo=nodo.moverCoor(dire)
		if(nextNodo not in caminos ):
			if(tirarPared(tablero,nodo,dire)):
				caminos.append(nextNodo)
				caminosf.append(nextNodo)
		terminado=True
		for d in Direccion:
			if((nodo.moverCoor(d) not in caminos) and ((d==Direccion.arriba and nodo.coory!=0)or(d==Direccion.derecha and nodo.coorx!=size-1) or (d==Direccion.abajo and nodo.coory!=size-1) or (d==Direccion.izquierda and nodo.coorx!=0))):
				terminado=False
		if terminado:
			caminosf.remove(nodo)
	salida=coordenada(randint(0,size-1),size-1)
	tirarES(tablero,salida,Direccion.abajo)
	for i in range(n//20):
		nodo=caminos[randint(0,len(caminos)-1)]
		dire=dirAl()
		tirarPared(tablero,nodo,dire)
	return (entrada,salida)





def dirAl():#direccion aleatoria
	n=randint(0,3)
	if(n==0):
		return Direccion.arriba
	elif(n==1):
		return Direccion.derecha
	elif(n==2):
		return Direccion.abajo
	elif(n==3):
		return Direccion.izquierda







verticesCreados=[]
def crearGrafo(tablero,origen,salida):
  global verticesCreados
  vert=vertice(origen)
  verticesCreados=[vert]
  for d in Direccion:
    if d!=Direccion.arriba and comprobarConexion(tablero,origen,d):
      grafoRec(tablero,vert,origen.moverCoor(d),invDir(d),salida)

  return vert
def grafoRec(tablero,verticeOrigen,siguienteCoor,dirOrigen,salida):
  global verticesCreados
  conection=[]
  camino=[verticeOrigen.obtenerPosicion()]
  actual=siguienteCoor
  cantidad=1
  while(cantidad==1):
    conection=[]
    camino.append(actual)
    for d in Direccion:
      if d!=dirOrigen and comprobarConexion(tablero,actual,d):
        conection.append(d)

    cantidad=len(conection)

    if cantidad==1:
      if actual==salida:
        sinSalida=vertice(actual)
        verticesCreados.append(sinSalida)
        verticeOrigen.agregarVecino(sinSalida,camino)
        sinSalida.agregarVecino(verticeOrigen,camino)
        return
      actual=actual.moverCoor(conection[0])
      dirOrigen=invDir(conection[0])
  if cantidad==0:
    sinSalida=vertice(actual)
    verticesCreados.append(sinSalida)
    verticeOrigen.agregarVecino(sinSalida,camino)
    sinSalida.agregarVecino(verticeOrigen,camino)
  else:
    nuevoVertice=vertice(actual)
    if nuevoVertice in verticesCreados:
      v=verticesCreados[verticesCreados.index(nuevoVertice)]
      if verticeOrigen in v.obtenerConexiones():
        if len(camino)-1<v.obtenerDistancia(verticeOrigen):
          v.agregarVecino(verticeOrigen,camino)
          verticeOrigen.agregarVecino(v,camino)
      else:
        v.agregarVecino(verticeOrigen,camino)
        verticeOrigen.agregarVecino(v,camino)
    else:
      verticesCreados.append(nuevoVertice)
      verticeOrigen.agregarVecino(nuevoVertice,camino)
      nuevoVertice.agregarVecino(verticeOrigen,camino)
      for d in conection:
        if actual!=salida or d!=Direccion.abajo:
          grafoRec(tablero,nuevoVertice,actual.moverCoor(d),invDir(d),salida)


verticesImpresos=[]
def imprimirGrafo(vert,ant=vertice(coordenada(100,100))):
  global verticesImpresos
  if vert not in verticesImpresos:
    print(str(vert))
    verticesImpresos.append(vert)
    for v in vert.obtenerConexiones():
      if v!=ant:
        imprimirGrafo(v,vert)

def djikstra(vertin,vertout):
  costos={}
  definitivos=[]
  costos[vertin]=(None,0)
  while(vertout not in definitivos):
    #print([str(a.obtenerPosicion())+" "+str(b[0])+" "+str(b[1]) for a,b in costos.items()],[str(a.obtenerPosicion())for a in definitivos])
    vertMenor=None
    menor=0
    for vert in list(costos.keys()):
      if (None==vertMenor or costos[vert][1] < menor) and vert not in definitivos:
        menor=costos[vert][1]
        vertMenor=vert
    definitivos.append(vertMenor)
    #print(str(vertMenor.obtenerPosicion()),end="")
    for v in vertMenor.obtenerConexiones():
      #print(str(v.obtenerPosicion()),end="")
      if v not in definitivos:
        costo=menor+vertMenor.obtenerDistancia(v)
        if(v not in costos) or (costos[v][1]>costo):
          costos[v]=(vertMenor,costo)
    #print("")
  solucion=[]
  origen=definitivos[definitivos.index(vertout)]
  while(origen!=None):
    #print(str(origen))
    preOrigen=costos[origen][0]
    #print(str(preOrigen))
    if preOrigen!=None:
      solucion+=origen.obtenerCamino(preOrigen)
    origen=preOrigen
  return solucion

def posicionDelJugador(coordenada,inputKey,tablero):
  if(comprobarConexion(tablero,coordenada,direccionJugador(inputKey))):
    return(coordenada.moverCoor(direccionJugador(inputKey)))
  else:
    return(coordenada)

def direccionJugador(inputKey):

  if(inputKey == "w" or inputKey == "W"):
    return Direccion.arriba
  elif(inputKey == "a" or inputKey == "A" ):
    return Direccion.izquierda
  elif (inputKey == "s" or inputKey == "S" ):
    return Direccion.abajo
  elif(inputKey == "d" or inputKey == "D"):
    return Direccion.derecha
