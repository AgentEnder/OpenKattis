import sys
line = sys.stdin.readline().replace("\n", "").split(" ")

repeats = False
for word in line:
	if line.count(word) > 1:
		print("no")
		repeats = True
		break
if repeats == False:
	print("yes")