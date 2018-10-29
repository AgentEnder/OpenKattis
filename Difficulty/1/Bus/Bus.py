#Bus, OpenKattis, https://open.kattis.com/problems/bus
## Sln by Craigory Coppola
import sys
for test_case in range(int(sys.stdin.readline())):
	people = 1
	for i in range(int(sys.stdin.readline())-1):
		people = (people+.5)*2
	print(int(people))