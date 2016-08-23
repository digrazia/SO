from tabulate import tabulate
class Memory():

	def __init__(self):
		self._memory = []

	def load(self, program):
		self._memory = program.instructions

	def fetch(self, addr):
		return self._memory[addr]

	def __repr__(self):
		return tabulate(enumerate(self._memory), tablefmt='psql')
