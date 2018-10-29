import sys


memoise = {}
def get_boxes_in(bx, diag):
	def traversal(start, graph, outer = []):
		if start not in memoise:
			memoise[start] = [start]
		else:
			return memoise[start]
		for child_box in graph[bx]:
			memoise[start].append(child_box)
			for parent in outer:
				memoise[parent].append(child_box)
			traversal(child_box, graph, outer + [start])
	traversal(bx, diag)
	return memoise[bx]
			

n = int(sys.stdin.readline())
box_diagram = {x+1:[] for x in range(n)}
for idx, box in enumerate(sys.stdin.readline().split(),1):
	box=int(box)
	if box not in box_diagram:
		box_diagram[box] = []
	box_diagram[box].append(idx)
	
for query_idx in range(int(sys.stdin.readline())):
	query = [int(x) for x in sys.stdin.readline().split()][1:]
	boxes = set()
	for box in query:
		for bx in get_boxes_in(box, box_diagram):
			boxes.add(bx)
	print(boxes)
	print(len(boxes))
	