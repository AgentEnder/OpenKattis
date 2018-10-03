#Problem: Aaah! from kattis, https://open.kattis.com/problems/aaah
#Sln by Craigory Coppola
import sys

marcus_ah = len(sys.stdin.readline())
dr_ah = len(sys.stdin.readline())

if marcus_ah >= dr_ah:
	print("go")
else:
	print("no")