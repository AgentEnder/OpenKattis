#Playfaire Cipher, OpenKattis, https://open.kattis.com/problems/playfair
#Sln by Craigory Coppola
import sys

cipher_grid = ["a" for x in range(25)] # x= idx%5, y = idx//5
letters = "abcdefghijklmnoprstuvwxyz"

key = sys.stdin.readline().replace("\n", "").lower().replace(" ", "")
working_key = key
cipher_idx = 0
while len(working_key) >= 1:
	char = working_key[0]
	cipher_grid[cipher_idx] = char
	working_key = working_key.replace(char, "")
	letters = letters.replace(char, "")
	cipher_idx+=1
while cipher_idx < 25:
	char = letters[0]
	cipher_grid[cipher_idx] = char
	letters = letters.replace(char, "")
	cipher_idx+=1

cipher_grid = "".join(cipher_grid)

msg = sys.stdin.readline().replace("\n", "").replace(" ", "")
msg_pairs = []
while len(msg) > 1:
	if msg[0] == msg[1]:
		msg_pairs.append([msg[0], 'x'])
		msg = msg[1:]
	else:
		msg_pairs.append(list(msg[:2]))
		msg = msg[2:]
if len(msg) > 0:
	msg_pairs.append(list(msg[0] + "x"))

cipher_text = ""
for pair in msg_pairs:
	idx1 = cipher_grid.find(pair[0])
	x1 = idx1 % 5
	y1 = idx1 // 5
	idx2 = cipher_grid.find(pair[1])
	x2 = idx2 % 5
	y2 = idx2 // 5
	
	if(y1 == y2): #Same Row
		x1 = (x1+1)%5
		x2 = (x2+1)%5
		cipher_text+=(cipher_grid[y1*5+x1])
		cipher_text+=(cipher_grid[y2*5+x2])
	elif(x1 == x2): #Same Column
		y1 = (y1+1)%5
		y2 = (y2+1)%5
		cipher_text+=(cipher_grid[y1*5+x1])
		cipher_text+=(cipher_grid[y2*5+x2])
	else:
		cipher_text+=(cipher_grid[y1*5+x2])
		cipher_text+=(cipher_grid[y2*5+x1])
print(cipher_text.upper())