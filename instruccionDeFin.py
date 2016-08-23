from instruccion import *

class InstruccionDeFin(Instruccion):

	def ejecutateEn(self,unCpu):
		unCpu.detener("fin del programa")

	def __repr__(self):
		return "FIN"
