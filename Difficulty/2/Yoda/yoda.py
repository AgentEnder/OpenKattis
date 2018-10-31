#Yoda, OpenKattis, https://open.kattis.com/problems/yoda
#Sln by Craigory Coppola

import sys

digits1 = [int(x) for x in list(input())]
digits2 = [int(x) for x in list(input())]
while len(digits1) != len(digits2):
	if len(digits1) < len(digits2):
		digits1.insert(0,0)
	else:
		digits2.insert(0,0)
		
for idx in range(len(digits1)):
	if digits1[idx] == digits2[idx]:
		continue
	if digits1[idx] < digits2[idx]:
		digits1[idx] = -1
	else:
		digits2[idx] = -1

def isNeg(n):
	return not (n<0)

if max(digits1) == -1:
	print("YODA")
else:
	print(eval("".join([str(x) for x in filter(isNeg, digits1)])))
	
if max(digits2) == -1:
	print("YODA")
else:
	print(eval("".join([str(x) for x in filter(isNeg, digits2)])))
