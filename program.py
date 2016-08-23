from instruccionDeFin import *
from instruccionDeIO import *
from instruccionDeCpu import *



class Program():

	def __init__(self, name, instructions):
		self._name = name
		self._instructions = self.expand(instructions)

	@property
	def name(self):
		return self._name

	@property
	def instructions(self):
		return self._instructions

	def expand(self, instructions):
		expanded = []
		for instr in instructions:
			expanded.extend(instr.expand())
		expanded.append(InstruccionDeFin())
		return expanded

	def __repr__(self):
		return "Program("+self.name+","+str(self.instructions)+")"
