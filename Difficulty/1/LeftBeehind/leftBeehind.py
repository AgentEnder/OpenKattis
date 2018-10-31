#Left Beehind, OpenKattis, https://open.kattis.com/problems/leftbeehind
#Sln by Craigory Coppola
while True:
	line = [int(x) for x in input().split()]
	if line == [0,0]:
		break
	elif sum(line) == 13:
		print("Never speak again.")
	elif line[1] > line[0]:
		print("Left beehind.")
	elif line[0]>line[1]:
		print("To the convention.")
	else:
		print("Undecided.")