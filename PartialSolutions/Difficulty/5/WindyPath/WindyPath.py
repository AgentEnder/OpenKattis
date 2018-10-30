#Windy Path, OpenKattis, https://open.kattis.com/problems/windypath
import sys, copy

points = {}
num_points = int(sys.stdin.readline())
for point_idx in range(num_points):
	points[point_idx+1] = [int(x) for x in sys.stdin.readline().split()]
dir = sys.stdin.readline().replace("\n","")

def solve():
	dir_idx = 0
	def backtracker(curr_point,remaining_points = copy.deepcopy(points), path = [], dir_idx = 0):
		print(len(path), path)
		if len(path) < 2:
			path.append(curr_point)
			for point in remaining_points.keys():
				backtracker(point, {x:remaining_points[x] for x in remaining_points.keys() if x != point}, path)
		elif len(path) == num_points :
			print("PATH: ", path)
		else:
			for point_name, point in remaining_points.items():
				new_vector = [point[0]-points[path[len(path)-1]][0], point[1]-points[path[len(path)-1]][1]]
				old_vector = [points[path[len(path)-1]][0] - points[path[len(path)-2]][0],points[path[len(path)-1]][1] - points[path[len(path)-2]][1]]
				curr_dir = ""
				if old_vector[0] == 0:
					if old_vector[1] > 0:
						if new_vector[0] < 0:
							curr_dir = "L"
						else:
							curr_dir = "R"
					else:
						if new_vector[0] < 0:
							curr_dir = "R"
						else:
							curr_dir = "L"
				elif new_vector[0] == 0:
					if old_vector[0] < 0:
						if new_vector[1] > 0:
							curr_dir = "R"
						else:
							curr_dir = "L"
					else:
						if new_vector[1] > 0:
							curr_dir = "L"
						else:
							curr_dir = "R"
				print(old_vector, "->", new_vector)
				if curr_dir == dir[dir_idx]:
					path.append(point_name)
					dir_idx+=1
					backtracker(point_name, {x:remaining_points[x] for x in remaining_points.keys() if x != point_name}, path)
	for point in points.keys():
		backtracker(point, copy.deepcopy(points), [point], 0)
print(points)
solve()
			
			