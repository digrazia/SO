#!/usr/bin/env python3

from program import *
from so import *
if __name__ == '__main__':
	p = Program("test.exe", [InstruccionDeCPU(5), InstruccionDeIO(2), InstruccionDeCPU(3)])
	so = SO()
	so.exec(p)