#Reverse Rot, OpenKattis, https://open.kattis.com/problems/reverserot
#Sln by Craigory Coppola

import sys

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
int_map = {chars[c]:c for c in range(len(chars))}

while True:
	line = sys.stdin.readline()
	line = line.replace("\n", "")
	line = line.split(" ")
	if len(line) == 1:
		break
	else:
		rot = int(line[0])
		reversed_msg = line[1][::-1]
		ciphertext = "".join(chars[(int_map[x]+rot)%len(chars)] for x in reversed_msg)
		print(ciphertext)