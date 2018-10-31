#Number Fun, OpenKattis, https://open.kattis.com/problems/numberfun
#Sln by Craigory Coppola
test_cases = int(input())
for test_id in range(test_cases):
	line = [int(x) for x in input().split()]
	if line[0]+line[1]==line[2]:
		print("Possible")
	elif line[0]*line[1]==line[2]:
		print("Possible")
	elif line[1]-line[0]==line[2]:
		print("Possible")
	elif line[0]-line[1]==line[2]:
		print("Possible")
	elif line[1]/line[0] ==line[2]:
		print("Possible")
	elif line[0]/line[1] ==line[2]:
		print("Possible")
	else:
		print("Impossible")