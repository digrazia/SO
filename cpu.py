
class Cpu():

	def __init__(self, meme):
		self._memory = meme
		self._pc = 0

	def start(self):
		self._continuarEjecucion =True
		while self._continuarEjecucion:
			op = self._memory.fetch(self._pc)
			self._tick(op)

	def detener(self,motivo):
		self._continuarEjecucion = False
		print("\tse detiene la ejecucion del programa por:",motivo)

	@property
	def pc(self):
		return self._pc

	@pc.setter
	def pc(self, addr):
		self._pc = addr

	def _tick(self, op):
		print("Exec: {op}\t PC={pc}".format(op=op, pc=self._pc))
		op.ejecutateEn(self)
		self._pc += 1

	def __repr__(self):
		return "CPU("+str(self._pc)+")"
