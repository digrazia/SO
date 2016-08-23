#!/usr/bin/env python3
from tabulate import tabulate
from time import sleep

class Instruccion():

	def __init__(self,ciclosDeEjecucion=1):
		self._ciclosDeEjecucion = ciclosDeEjecucion

	@property
	def ciclosDeEjecucion(self):
		return self._ciclosDeEjecucion

	def expand(self):
		expanded = []
		for _ in range(self._ciclosDeEjecucion):
			expanded.append(self.__class__(0))
		return expanded

	def ejecutateEn(self,unCpu):
		sleep(1)