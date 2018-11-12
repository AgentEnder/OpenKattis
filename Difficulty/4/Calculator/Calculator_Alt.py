#Calculator, OpenKattis, https://open.kattis.com/problems/calculator
#Sln by Craigory Coppola
import sys
for line in sys.stdin:
	print('%.2f' % eval(line))