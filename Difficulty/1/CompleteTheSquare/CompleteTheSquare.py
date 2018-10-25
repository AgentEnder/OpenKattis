#CompleteTheSquare, OpenKattis, https://open.kattis.com/problems/completingthesquare
##Partial Sln by Craigory Coppola (Wrong Answer on Test Case 6
import sys, math

a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]
c = [int(x) for x in sys.stdin.readline().split()]

def add(pt1, pt2):
	return [pt1[0]+pt2[0],pt1[1]+pt2[1]]
def subtract(pt1, pt2):
	return [pt1[0]-pt2[0],pt1[1]-pt2[1]]
	
def checkPerp(v1, v2):
	return (v1[0]*v2[0]+v1[1]*v2[1] == 0)
	
if checkPerp(subtract(a,b), subtract(a,c)):
	AB = subtract(b,a)
	AC = subtract(c,a)
	D = add(c,add(AB,AC))
	print(D[0], D[1])
elif checkPerp(subtract(b,a), subtract(b,c)):
	BA = subtract(a,b)
	BC = subtract(c,b)
	D = add(b,add(BA,BC))
	print(D[0], D[1])
elif checkPerp(subtract(c,a), subtract(c,b)):
	CA = subtract(a,c)
	CB = subtract(b,c)
	D = add(c,add(CA,CB))
	print(D[0], D[1])
