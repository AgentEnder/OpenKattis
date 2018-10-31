#Trimming Convex Polygons, OpenKattis, https://open.kattis.com/problems/trimmingpolygons
#Partial Sln, By Craigory Coppola. Breaks due to case when you should not remove the largest point, but should remove the next largest.
import sys

def get_subsets(n, max):
	subsets = []
	
	

def polygon_area(points):
	if len(points) < 3:
		return 0
	elif len(points) == 3:
		return triangle_area(points)
	points = sorted(points, key=lambda point:point[2]) 
	triangles = []
	pivot = points[0]
	for vertex_id in range(len(verticies)-1):
		triangles.append([pivot, verticies[vertex_id],  verticies[vertex_id+1]])
	area = sum([triangle_area(t) for t in triangles])
	return(area)

def triangle_area(points):
	return abs((points[0][0]*(points[1][1]-points[2][1])+points[1][0]*(points[2][1]-points[0][1])+points[2][0]*(points[0][1]-points[1][1]))/2)
	
num_verticies = int(sys.stdin.readline())
verticies = []

for idx in range(num_verticies):
	line = [int(x) for x in sys.stdin.readline().split()]
	verticies.append(line)

verticies.sort(key=lambda point:point[2])
maximum_value = 0
for sell_points in range(1,len(verticies)+1):
	illegal = sum([i[2] for i in verticies[-sell_points:]])
	legal = 2*polygon_area([[vertex[0],vertex[1]] for vertex in verticies[:-sell_points]])
	new_value = legal + illegal
	if new_value > maximum_value:
		maximum_value = new_value
if int(maximum_value) == maximum_value:
	print(int(maximum_value))
else:
	print(maximum_value)