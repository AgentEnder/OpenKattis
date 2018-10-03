#Different Distances, OpenKattis, https://open.kattis.com/problems/differentdistances
#Sln by Craigory Coppola
import sys

while True:
	line = sys.stdin.readline()
	if len(line.split(" ")) < 5:
		break
	else:
		line = [float(line.split(" ")[x]) for x in range(5)]
		print( (abs(line[2]-line[0])**line[4]+abs(line[3]-line[1])**line[4])**(1/line[4]))