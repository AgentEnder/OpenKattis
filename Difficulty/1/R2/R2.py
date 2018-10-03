#Problem R2 from Kattis, https://open.kattis.com/problems/r2
#Sln by Craigory Coppola

import sys

line = sys.stdin.readline()
line = line.split(" ")
R1 = int(line[0])
S = int(line[1])
print(R1+(S-R1)*2)