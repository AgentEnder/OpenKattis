#3d Printed Statues, OpenKattis, https://open.kattis.com/problems/3dprinter
#Sln by Craigory Coppola

import sys

num_statues = int(sys.stdin.readline())

num_days = 0
printers = 1

while num_statues > 2*printers:
	printers*=2
	num_days+=1

statues = 0
while statues < num_statues:
	statues+=printers
	num_days+=1
	
print(num_days)