#Test Generator for AnotherQueryOnArray, OpenKattis

import random

num_case = 0

def gen():
	global num_case
	n = random.randint(1,10**5)
	m = random.randint(1,10**5)
	operations = []
	for i in range(m):
		xy = [random.randint(0,n),random.randint(0,n)]
		operations.append([random.randint(0,2), min(xy), max(xy)])
	with open("test"+str(num_case)+".in", "w") as testfile:
		testfile.write(str(n)+" "+str(m)+"\n")
		for oper in operations:
			testfile.write(str(oper[0]) + " " + str(oper[1]) +" " + str(oper[2]) + "\n")
			
for i in range(100):
	gen()
	num_case+=1
	