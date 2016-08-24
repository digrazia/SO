#!/usr/bin/env python3

from memoria import *
from cpu import *

class SO():

	def __init__(self):
		self._memory = Memory()
		self._cpu = Cpu(self._memory)

	def exec(self, prog):
		self._memory.load(prog)
		print(self)
		self._cpu.pc = 0
		self._cpu.start()

	def __repr__(self):
		return self._cpu.__repr__() +"\n"+self._memory.__repr__()
