from instruccion import *

class InstruccionDeCPU(Instruccion):

	def __repr__(self):
			return "Cpu("+str(self._ciclosDeEjecucion )+")"
