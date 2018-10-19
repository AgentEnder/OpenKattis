#Encoded Message, OpenKattis, https://open.kattis.com/problems/encodedmessage
## Sln by Craigory Coppola

import sys
import math

test_cases = int(sys.stdin.readline())
for test_case in range(test_cases):
	ciphertext = sys.stdin.readline().replace("\n","")
	dimen = int(math.sqrt(len(ciphertext)))
	for j in reversed(range(dimen)):
		for i in range(dimen):
			print(ciphertext[dimen*(i)+j], end="")
	print()