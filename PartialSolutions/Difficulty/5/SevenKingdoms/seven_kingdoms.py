#import resource
import sys

# Will segfault without this line.
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)


def BronKerbosch(graph, node): #P is nodes in graph
	report = set()
	def BronKerboschHelper(r=set(),p=set(graph[node]+[node]),x=set()):
		if len(p) == 0 and len(x) == 0:
			report.add(frozenset(r))
		for vertex in p:
			BronKerboschHelper(r.union(set([vertex])), set(p).intersection(graph[vertex]), x.intersection(graph[vertex]))
			p = p.difference([vertex])
			x = x.union([vertex])
	BronKerboschHelper()
	max_clique = set()
	for clique in report:
		if len(clique) > len(max_clique):
			max_clique = clique
	return max_clique

"""
def get_maximal_clique_for_node(graph, node):
	cliques = [set()]
	def clique_finder(current, seen = [], clique = [], remaining = []):
		if current in seen:
			return
		for c_node in clique:
			if c_node not in graph[current]+[current]:
				break
		else:
			clique.add(current)
		for connected_node in remaining.difference(clique).difference(set([current])):
			clique_finder(connected_node, seen, clique, remaining)
		else:
			if len(cliques[0]) < len(clique):
				cliques[0] = clique
	clique_finder(node, [], set(), set(graph[node]))
	return cliques[0]"""


	
num_nodes, num_edges = [int(x) for x in input().split()]
if num_edges == 0:
	if num_nodes <= 3:
		print(1)
		print(2)
	else:
		print("impossible")
else:
	graph = {}
	for edge_idx in range(num_edges):
		edge = [int(x) for x in input().split()]
		if edge[0] not in graph:
			graph[edge[0]] = []
		if edge[1] not in graph:
			graph[edge[1]] = []
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])

	arya_clique = BronKerbosch(graph,1)
	sansa_clique = BronKerbosch(graph,2)
	cities = set(sorted(graph.keys()))
	cities = cities.difference(arya_clique)
	cities = cities.difference(sansa_clique)
	jon_clique = BronKerbosch(graph, list(cities)[0])
	cities = cities.difference(jon_clique)
	if len(cities) == 0:
		for city in sorted(arya_clique):
			print(city, end=" ")
		print()
		for city in sorted(sansa_clique):
			print(city, end=" ")
		print
	else:
		print("impossible")