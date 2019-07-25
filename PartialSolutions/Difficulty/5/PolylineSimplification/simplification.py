#Polyline Simplification, OpenKattis, https://open.kattis.com/problems/simplification
#Sln by Craigory Coppola

import math

orig, desired = [int(x)+1 for x in input().split()]
points = [tuple(int(x) for x in input().split()) for line in range(orig)]
removed = []

while len(points) > desired:
	min_area = -1
	removal_point = -1
	for point_idx in range(1,len(points)-1):
		p0 = points[point_idx-1]
		p1 = points[point_idx]
		p2 = points[point_idx+1]
		area = abs((p0[0]*p1[1]+p1[0]*p2[1]+p2[0]*p0[1]-p0[1]*p1[0]-p1[1]*p2[0]-p2[1]*p0[0])/2)
		if min_area is -1 or area < min_area:
			min_area = area
			removal_point = point_idx
	p = removal_point
	for i in removed:
		if removal_point > i:
			p+=1
	print(p)
	removed.append(p)
	points = points[:removal_point] + points[removal_point+1:]
		