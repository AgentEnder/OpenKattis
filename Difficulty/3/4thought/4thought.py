#4 Thought, OpenKattis, https://open.kattis.com/problems/4thought
#Sln by Craigory Coppola

import sys

operators = {"*":"*","+":"+","-":"-","//":"/"}

functions = {}
test = []

for a in operators.keys():
	for b in operators.keys():
		for c in operators.keys():
			val = int(eval("4"+a+"4"+b+"4"+c+"4"))
			if not val in functions:
				functions[val]="4 "+operators[a]+" 4 "+operators[b]+" 4 "+operators[c]+" 4 = "+str(val)


test_cases = int(sys.stdin.readline())
for test_case in range(test_cases):
	val = int(sys.stdin.readline())
	if val in functions:
		print(functions[val])
	else:
		print("no solution")