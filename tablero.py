from coordenada import *
from direccion import *
def generarTablero(n):
	tablero =[[1 for x in range(n*2+1)] for y in range(n+1)]
	return tablero
def tamaño(tablero):
	return len(tablero)-1
def tirarPared(tablero,coordenada,direccion):

	i = coordenada.coorx
	j = coordenada.coory*2

	if(direccion==Direccion.abajo):
		j+=2
	elif(direccion==Direccion.izquierda):
		j+=1
	elif(direccion==Direccion.derecha):
		j+=1
		i+=1
	if(i==0 or i==len(tablero)-1 or j==0 or j==len(tablero[0])-1):
		return False
	tablero[i][j] = 0
	return True
def tirarES(tablero,coordenada,direccion):

	i = coordenada.coorx
	j = coordenada.coory*2

	if(direccion==Direccion.abajo):
		j+=2
	elif(direccion==Direccion.izquierda):
		j+=1
	elif(direccion==Direccion.derecha):
		j+=1
		i+=1
	tablero[i][j] = 0

def crearPared(tablero,coordenada,direccion):

	i = coordenada.coorx
	j = coordenada.coory*2

	if(direccion==Direccion.abajo):
		j+=2
	elif(direccion==Direccion.izquierda):
		j+=1
	elif(direccion==Direccion.derecha):
		j+=1
		i+=1

	tablero[i][j] = 1
	return tablero
def imprimirTablero(tablero,c1,c2,coorPisada = []):
  contPisada = 0
  if(len(tablero[0])<(c2.coory+1) or len(tablero)*2<((c2.coorx)+1)):#Corregir cuando se genere la matriz programaticamente
	  print("La matriz no es del tamaño indicado")
	  return
  pared= "\u2588"*2
  camino="  "
  pisada="\u259A"*2 #"\u259A"#+"\u259A"
  for j in range(c1.coory,c2.coory+1):
    print(pared,end="")
    for i in range(c1.coorx,c2.coorx+1):
      if (comprobarConexion(tablero,coordenada(i,j),Direccion.arriba)):
        print(camino+pared,end="")
      else:
        print(pared*2,end="")
    print("")
    if(comprobarConexion(tablero,coordenada(0,j),Direccion.izquierda)):
      print(camino,end="")
    else:
      print(pared,end="")
    for i in range(c1.coorx,c2.coorx+1):
      coordenadaAux=coordenada(i,j)
      if(comprobarConexion(tablero,coordenada(i,j),Direccion.derecha)):
        if coordenadaAux in coorPisada:
          print(pisada+camino,end="")
        else:
          print(camino*2,end="")
      else:
          if coordenadaAux  in coorPisada:
            print(pisada+pared,end="")
          else:
            print(camino+pared,end="")
    print("")
  print(pared,end="")
  for i in range(c1.coorx,c2.coorx+1):

    if(comprobarConexion(tablero,coordenada(i,c2.coory+1),Direccion.arriba)):
      print(camino+pared,end="")
    else:
      print(pared*2,end="")
  print("")


def comprobarConexion(tablero,coordenada,direccion):

	i = coordenada.coorx
	j = coordenada.coory*2

	if(direccion==Direccion.abajo):
		j+=2
	elif(direccion==Direccion.izquierda):
		j+=1
	elif(direccion==Direccion.derecha):
		j+=1
		i+=1
	#print(i,j,end="")
	if(tablero[i][j] == 0):
		return True
	return False
