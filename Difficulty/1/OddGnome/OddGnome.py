#Odd Gnome, OpenKattis, https://open.kattis.com/problems/oddgnome
## Sln by Craigory Coppola

import sys

test_cases = int(sys.stdin.readline())

for test_case in range(1,test_cases+1):
	line = sys.stdin.readline().split()
	group = [int(x) for x in line[1:]]
	for idx, value in enumerate(group):
		if idx == 0:
			continue
		if value != group[idx-1]+1:
			print(idx+1)
			break