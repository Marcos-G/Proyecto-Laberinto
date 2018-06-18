from coordenada import *
from algoritmos import *
from camino import *
from tablero import*
import threading
import queue
import sys
import io
import os
tam=15

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
def hilo(tablero,queue):
  (entrada,salida)=crearLaberinto(tablero)
  queue.put((entrada))
  queue.put((salida))
def esclavosResuelvan(tablero,entrada,salida):
  lista = []
  verticeEntrada=crearGrafo(tablero,entrada,salida)
  verticeSalida=vertice(salida)
  lista = djikstra(verticeEntrada,verticeSalida)
  imprimirTablero(tablero,coordenada(0,0),coordenada(tam-1,tam-1),lista)

def jugar(tablero,coordenada,inputKey):
  return posicionDelJugador(coordenada,inputKey,tablero)

inputKey = "Ready"

while inputKey != "exit":

  tablero=generarTablero(tam)

  my_queue = queue.Queue()
  hilo1 = threading.Thread(target=hilo,args=(tablero,my_queue))
  hilo1.start()

  print("<Bievenido joven viajero programador, estas por aventurarte en el laberinto de la muerte TAD> \n")

  modo = -1

  while modo < 0 or modo > 3 or type(modo)!=type(1):

    print ("Elige un modo de dificultad:\n")

    print("1 - Modo Omnipresente: (Si no te la aguantas como el rulo) resuelves el laberinto por ti mismo, tienes la capacidad de ver todo el laberinto \n")

    print("2 - Modo Gamer: resolve el laberinto sin saber hacia donde vas \n")
    print("3 - Modo observador: Tus esclavos resuelven el camino por ti \n")

    modo = input("Elige sabiamente => \n")

    if(modo!='1' and modo!='2'):
      print("modo inexistente \n")
    else:
      modo=int(modo)
      #(entrada,salida)= my_queue.get()
      os.system("clear")
      print("CARGANDO")
      (entrada)= my_queue.get()
      (salida)= my_queue.get()
      #os.system("clear")
      if(modo == 1):
        os.system("clear")
        coordJugador=coordenada(entrada.coorx,entrada.coory)
        aux=[coordJugador]
        imprimirTablero(tablero,coordenada(0,0),coordenada(tam-1,tam-1),aux)
        while salida != coordJugador:
          inputKey = str(input("Ingrese una tecla de direccion (w,a,s,d) o r para rendirse \n"))
          if(inputKey == "r"):
            os.system("clear")
            esclavosResuelvan(tablero,entrada,salida)
            break
          coordJugador = jugar(tablero,coordJugador,inputKey)
          aux.pop()
          aux.append(coordJugador)
          os.system("clear")
          imprimirTablero(tablero,coordenada(0,0),coordenada(tam-1,tam-1),aux)
        print("HAS LOGRADO ESCAPAR... POR AHORA")
      elif(modo == 2):
          os.system("clear")
          coordJugador=coordenada(entrada.coorx,entrada.coory)
          aux=[coordJugador]
          imprimirTablero(tablero,coordenada(max(0,coordJugador.coorx-3),max(0,coordJugador.coory-3)),coordenada(min(tam-1,coordJugador.coorx+3),min(tam-1,coordJugador.coory+3)),aux)
          while salida != coordJugador:
            inputKey = str(input("Ingrese una tecla de direccion (w,a,s,d) o r para rendirse \n"))
            if(inputKey == "r"):
              os.system("clear")
              esclavosResuelvan(tablero,entrada,salida)
              break
            coordJugador = jugar(tablero,coordJugador,inputKey)
            aux.pop()
            aux.append(coordJugador)
            os.system("clear")
            imprimirTablero(tablero,coordenada(max(0,coordJugador.coorx-3),max(0,coordJugador.coory-3)),coordenada(min(tam-1,coordJugador.coorx+3),min(tam-1,coordJugador.coory+3)),aux)
          print("HAS LOGRADO ESCAPAR... POR AHORA")
      elif(modo == 3):
        os.system("clear")
        esclavosResuelvan(tablero,entrada,salida)

      #LLAMAR FUNCION DE EDGAR

	    #Se muestra todo el laberinto y abria que pasarle una nueva variabe a la de imprimir, llamar a la funcion jugar()
	    #imprimirTablero(tablero,obtenerCoordenada(tablero,0),obtenerCoordenada(tablero,1))
    #elif(modo == 2):
	    #imprimirTablero(tablero,10,10)
	    #jugar()
    #elif(modo == 3):
	    #resolverLaberinto
	    #imprimirTablero(tablero,10,10)



  inputKey = "exit"
