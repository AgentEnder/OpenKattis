#SodaSurpler from OpenKattis https://open.kattis.com/problems/sodasurpler
#Sln by Craigory Coppola
import sys
import math

def solve(start, req):
	if start<req:
		return 0
	bottles = start%req
	bottles += start//req
	return start//req + solve(bottles, req)

line = sys.stdin.readline()
line = [int(line.split(" ")[x]) for x in range(3)]
start_bottles = line[0] + line[1]
bottles_required = line[2]

print(solve(start_bottles, bottles_required))