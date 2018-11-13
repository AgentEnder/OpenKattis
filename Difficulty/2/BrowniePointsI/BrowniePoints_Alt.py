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
		mod_point = [point[x]-mid_point[x] for x in range(2)]
		sum_abs_point = sum([abs(x) for x in mod_point])
		sum_mod_point = sum(mod_point)
		
		if sum_abs_point == 0:
			continue
		elif abs(sum_mod_point) < sum_abs_point:
			ollie_score+=1
		else:
			stan_score+=1
	print(stan_score,ollie_score)
