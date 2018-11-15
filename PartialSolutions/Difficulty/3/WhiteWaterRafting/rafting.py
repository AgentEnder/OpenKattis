import math

def dist(x1,y1,x2,y2):
	return(math.sqrt((x1-x2)**2+(y1-y2)**2))
	
for test_case in range(1,int(input())+1):
	max_size = None
	inner_polygon = [[int(ord) for ord in input().split()] for x in range(int(input()))]
	outer_polygon = [[int(ord) for ord in input().split()] for x in range(int(input()))]
	for inner_point in inner_polygon:
		curr_min = None
		for outer_point in sorted(outer_polygon, key=sum):
			distance = min(dist(inner_point[0],inner_point[1],outer_point[0], outer_point[1]), dist(inner_point[0],inner_point[1], outer_point[0],inner_point[1]), dist(inner_point[0],inner_point[1],inner_point[0],outer_point[1]))
			print(distance)
			if curr_min == None:
				curr_min = distance
			elif distance < curr_min:
				curr_min = distance
			else:
				break
		if max_size == None or curr_min < max_size:
			max_size = curr_min
	print("OUTPUT: ",max_size)