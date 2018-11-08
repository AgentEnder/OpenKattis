#Goat Ropes, OpenKattis, https://open.kattis.com/problems/goatropes
#Sln by Craigory Coppola
def distance(n1, n2):
	return round_to_two(((n1[0]-n2[0])**2+(n1[1]-n2[1])**2)**(1/2))

def round_to_two(n):
	return int(n*100+.5)/100.0

num_nodes = int(input())

nodes = [[int(x) for x in input().split()] for i in range(num_nodes)]
rope_used = 0
for idx, node in enumerate(nodes):
	max_rope = None
	for connecting_node in nodes:
		if node is connecting_node:
			continue
		dist = distance(node, connecting_node)/2
		print(node,"->",connecting_node, dist)
		if max_rope == None or max_rope>dist:
			max_rope = dist
	rope_used+=max_rope
	print("CONSUMED:", max_rope)
print(rope_used)