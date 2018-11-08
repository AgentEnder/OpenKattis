#Brownie Points I, OpenKattis, https://open.kattis.com/problems/browniepoints
#Sln by Craigory Coppola
import math

while True:
	in_stream = [int(x) for x in input().split()]
	if len(in_stream) == 1 and in_stream[0] == 0:
		break
	stan_score = 0
	ollie_score = 0
	points = [[int(x) for x in input().split()] for i in range(in_stream[0])]
	mid_point = points[len(points)//2]
	for point in points:
		if point[0]-mid_point[0] < 0 and point[1]-mid_point[1] < 0:
			stan_score+=1
		elif point[0]-mid_point[0] > 0 and point[1]-mid_point[1] > 0:
			stan_score+=1
		elif point[0]-mid_point[0] > 0 and point[1]-mid_point[1] < 0:
			ollie_score+=1
		elif point[0]-mid_point[0] < 0 and point[1]-mid_point[1] > 0:
			ollie_score+=1
	print(stan_score,ollie_score)