from instruccion import *

class InstruccionDeIO(Instruccion):

	def __repr__(self):
			return "IO("+str(self._ciclosDeEjecucion )+")"
