#Vin Diagrams, OpenKattis, https://open.kattis.com/problems/vindiagrams
#WIP by Craigory Coppola

import sys

def print_grid(grd):
	for line in grd:
		print(line)

def find_intersections(grd):
	inters = []
	for x in range(1, dimens[0]-1):
		for y in range(1, dimens[1]-1):
			if grd[x][y] == "X" and grd[x-1][y] == "X" and grd[x+1][y] == "X" and grd[x][y+1] == "X" and grd[x][y-1] == "X":
				inters.append([x,y])
	return inters

def empty_grid(x,y):
	return [[" " for y in range(dimens[1])] for x in range(dimens[0])]

def find_loops(start, grd):
	loops = {}
	current_loop = empty_grid(dimens[0], dimens[1])
	directions = ["up", "down", "left", "right"]
	def traverse_loop(current, grd, direction, start_point = None, name = None):
		current_loop[current[0]][current[1]] = "X"
		#print("ITER")
		#print_grid(current_loop)
		if grd[current[0]][current[1]] != "X":
			name = grd[current[0]][current[1]]
		if start_point == None:
			start_point = current
		elif start_point == current:
			if name != None:
				loops[name] = current_loop
			else:
				loops["Center"] = current_loop
			return
		if direction == "up":
			if current[1] > 0 and grid[current[0]][current[1]-1] != ".": #Can turn left
				traverse_loop([current[0],current[1]-1], grd, "left", start_point, name)
			elif current[0] > 0 and grid[current[0]-1][current[1]] != ".": #Can continue up
				traverse_loop([current[0]-1,current[1]], grd, "up", start_point, name)
			elif current[1]+1 < dimens[1] and grid[current[0]][current[1]+1] != ".": #Can turn right
				traverse_loop([current[0],current[1]+1], grd, "right", start_point, name)
			else:
				print("UP ELSE TRIGGERED")
		elif direction == "left":
			if current[0]+1 < dimens[0] and grid[current[0]+1][current[1]] != ".": #Can turn left, go down
				traverse_loop([current[0]+1,current[1]], grd, "down", start_point, name)
			elif current[1] > 0 and grid[current[0]][current[1]-1] != ".": #Can continue left
				traverse_loop([current[0],current[1]-1], grd, "left", start_point, name)
			elif current[0] > 0 and grid[current[0]-1][current[1]] != ".": #Can turn right, go up
				traverse_loop([current[0]-1,current[1]], grd, "up", start_point, name)
			else:
				print("LEFT ELSE TRIGGERED")
		elif direction == "down":
			if current[1]+1 < dimens[1] and grid[current[0]][current[1]+1] != ".": #Can turn left, go right
				traverse_loop([current[0],current[1]+1], grd, "right", start_point, name)
			elif current[0]+1 < dimens[0] and grid[current[0]+1][current[1]] != ".": #Can continue down
				traverse_loop([current[0]+1,current[1]], grd, "down", start_point, name)
			elif current[1] > 0 and grid[current[0]][current[1]-1] != ".": #Can turn right, go left
				traverse_loop([current[0],current[1]-1], grd, "left", start_point, name)
			else:
				print("DOWN ELSE TRIGGERED")
		elif direction == "right":
			if current[0] > 0 and grid[current[0]-1][current[1]] != ".": #Can turn left, go up
				traverse_loop([current[0]-1,current[1]], grd, "up", start_point, name)
			elif current[1]+1 < dimens[1] and grid[current[0]][current[1]+1] != ".": #Can continue right
				traverse_loop([current[0],current[1]+1], grd, "right", start_point, name)
			elif current[0]+1 < dimens[0] and grid[current[0]+1][current[1]] != ".": #Can turn right, go down
				traverse_loop([current[0]+1,current[1]], grd, "down", start_point, name)
			else:
				print("RIGHT ELSE TRIGGERED")
	for dir in directions:
		traverse_loop(start, grd, dir)
		current_loop = empty_grid(dimens[0], dimens[1])
	return loops
	
dimens = [int(x) for x in sys.stdin.readline().split()]
grid = [list(sys.stdin.readline().replace("\n", "")) for x in range(dimens[0])]



		
print_grid(grid)
intersections = find_intersections(grid)
for point in intersections:
	print("Intersection Point: ", point)
	loops = find_loops(point, grid)
	for key, value in loops.items():
		print(key,"---------------")
		print_grid(value)