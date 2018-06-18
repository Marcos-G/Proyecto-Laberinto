from direccion import *
class coordenada:
	coorx = None
	coory = None
	def __str__(self):
		return ("("+str(self.coorx)+","+str(self.coory)+")")
	def __eq__(self,other):
		return (self.coorx==other.coorx and self.coory==other.coory)
	def __ne__(self,other):
		return not (self.coorx==other.coorx and self.coory==other.coory)
	def __init__(self,x,y):
		self.coorx=x
		self.coory=y
	def moverCoor(self,dire):
		res=coordenada(self.coorx,self.coory)
		if(dire==Direccion.arriba):
			res.coory-=1
		elif(dire==Direccion.derecha):
			res.coorx+=1
		elif(dire==Direccion.abajo):
			res.coory+=1
		elif(dire==Direccion.izquierda):
			res.coorx-=1
		return res