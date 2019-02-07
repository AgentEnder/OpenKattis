#Counting Stars, OpenKattis, https://open.kattis.com/problems/countingstars
#Sln by Craigory Coppola



import sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


def findStar(curr_x, curr_y, w, h, grid, star = set()):
	curr = curr_y*w+curr_x
	if curr in star:
		return(set())
	star.add(curr)
	if (curr_x > 0 and grid[curr_y][curr_x-1] == "-"): # Left Check
		star.union(findStar(curr_x-1,curr_y, w, h, grid, star))
	if (curr_x < w-1 and grid[curr_y][curr_x+1] == "-"): # Right
		star.union(findStar(curr_x+1,curr_y, w, h, grid, star))
	if (curr_y > 0 and grid[curr_y-1][curr_x] == "-"): # Up Check
		star.union(findStar(curr_x,curr_y-1, w, h, grid, star))
	if (curr_y < h-1 and grid[curr_y+1][curr_x] == "-"): # Down Check
		star.union(findStar(curr_x,curr_y+1, w, h, grid, star))
	return star

case = 1
	
for line in sys.stdin:
	height, width = [int(x) for x in line.split()]
	grid = []
	for y in range(height):
		grid.append(list(input().strip()))
	stars = []
	star_count=0
	for y, row in enumerate(grid):
		for x, cell in enumerate(row):
			if cell == "-":
				curr = width*y+x
				for star in stars:
					if curr in star:
						break
				else:
					stars.append(findStar(x,y,width,height,grid, star = set()))
				
	res = "Case " + str(case) +  ": " + str(len(stars))
	print(res)
	case+=1
