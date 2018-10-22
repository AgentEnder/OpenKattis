#Oop, OpenKattis, https://open.kattis.com/problems/oop
#Partial Sln by Craigory Coppola, TOO SLOW
import sys, re

line = [int(x) for x in sys.stdin.readline().split()]
words = "\n".join([sys.stdin.readline().replace("\n", "") for i in range(line[0])])
patterns = [sys.stdin.readline().replace("\n", "") for i in range(line[1])]

data_bank = {}#[front, back]:

def checkPattern(ptn):
	r_ptn = re.compile(r"^" + ptn.replace('*','.*') + r"$", re.MULTILINE)
	if r_ptn in data_bank:
		return data_bank[r_ptn]
	data_bank[r_ptn] = len(re.findall(r_ptn, words))
	return data_bank[r_ptn]

for pattern in patterns:
	print(checkPattern(pattern))