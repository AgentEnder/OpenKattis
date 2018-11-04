#import resource
import sys

# Will segfault without this line.
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)


def BronKerbosch(graph): #P is nodes in graph
	report = set()
	def BronKerboschHelper(r=set(),p=set(graph.keys()),x=set()):
		if len(p) == 0 and len(x) == 0:
			report.add(frozenset(r))
		for vertex in p:
			BronKerboschHelper(r.union(set([vertex])), set(p).intersection(graph[vertex]), x.intersection(graph[vertex]))
			p = p.difference([vertex])
			x = x.union([vertex])
	BronKerboschHelper()
	return report
	
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

	sansa_cliques = []
	arya_cliques = []
	maximal_cliques = BronKerbosch(graph)
	for clique in maximal_cliques:
		if 1 in clique:
			arya_cliques.append([1])
			for city in clique:
				if city is not 1:
					arya_cliques[len(arya_cliques)-1].append(city)
		elif 2 in clique:
			sansa_cliques.append([2])
			for city in clique:
				if city is not 2:
					sansa_cliques[len(sansa_cliques)-1].append(city)
				
	cities = set(sorted(graph.keys()))
	solved = False
	for arya_clique in arya_cliques:
		for sansa_clique in sansa_cliques:
			remaining = cities.difference(set(sansa_clique)).difference(set(arya_clique))
			for clique in maximal_cliques:
				if len(remaining.difference(clique)) == 0:
					for city in sorted(arya_clique):
						print(city, end=" ")
					print()
					for city in sorted(sansa_clique):
						print(city, end=" ")
					print()
					solved=True
					break
			if solved:
				break
		if solved:
			break
	if not solved:
		print("impossible")