#Convex Polygon Area, OpenKattis, https://open.kattis.com/problems/convexpolygonarea
#Sln by Craigory Coppola

import math, sys

num_polygons = int(sys.stdin.readline())

def triangle_area(points):
	return abs((points[0][0]*(points[1][1]-points[2][1])+points[1][0]*(points[2][1]-points[0][1])+points[2][0]*(points[0][1]-points[1][1]))/2)
	

for idx in range(num_polygons):
	line = [int(x) for x in sys.stdin.readline().split()]
	num_verticies = line[0]
	pivot = [line[1],line[2]]
	verticies = [[line[2*i-1],line[2*i]] for i in range(2,num_verticies+1)] #remove first vertex, call it pivot
	triangles = []
	for vertex_id in range(len(verticies)-1):
		triangles.append([pivot, verticies[vertex_id],  verticies[vertex_id+1]])
	area = sum([triangle_area(t) for t in triangles])
	if int(area) == area:
		print(int(area))
	else:
		print(area)