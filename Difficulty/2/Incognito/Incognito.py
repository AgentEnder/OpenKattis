#Incognito, OpenKattis, https://open.kattis.com/problems/incognito
#Sln by Craigory Coppola, incomplete due to time.

import sys
	
test_cases = int(sys.stdin.readline())
for test_case in range(test_cases):
	num_attr = int(sys.stdin.readline())
	attr = {}
	for i in range(num_attr):
		line = sys.stdin.readline().replace("\n", "").split()
		key = line[1]
		value = line[0]
		if not key in attr.keys():
			attr[key] = []
		attr[key].append(value)
	outfits = 1
	for key, value in attr.items():
		outfits *= len(value)+1 #For each category add the option of not wearing anything from the category. Then simple multiply.
	print(outfits-1)
