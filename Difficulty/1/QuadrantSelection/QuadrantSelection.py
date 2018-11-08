#Quadrant Selection, OpenKattis, https://open.kattis.com/problems/quadrant
#Sln by Craigory Coppola
	
x,y = int(input()),int(input())
if x > 0:
	if y > 0:
		print(1)
	else:
		print(4)
else:
	if y > 0:
		print(2)
	else:
		print(3)