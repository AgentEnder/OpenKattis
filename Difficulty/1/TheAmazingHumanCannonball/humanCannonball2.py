#The Amazing Human Cannonball, OpenKattis, https://open.kattis.com/problems/humancannonball2
#Sln by Craigory Coppola
import math
test_cases = int(input())
for test_id in range(test_cases):
	v_0, theta, x_1, h_1, h_2 = [eval(x) for x in input().split()]
	t = x_1/(v_0*math.cos(math.radians(theta)))
	y = v_0*t*math.sin(math.radians(theta))-.5*9.81*t**2
	if y > h_1+1 and y < h_2-1:
		print("Safe")
	else:
		print("Not Safe")