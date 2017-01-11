"""Here we write an algo to determine all pairs shortest paths within a graph supplied as an edge list.
Edges can be negative, and we must report if there are negative cycles (cannot compute shortest paths if so)
We proceed via Johnson's algorithm, which is as follows:

1. Run Bellman Ford on the graph augmented with a source vertex connecting to every node with edge cost 0.
2. The shortest path lengths s-v to all vertices v are then used as the vertex weights,
such that the adjusted edge weights c_e' = c_e + p_u - p_v are all non-negative.
3. This allows us to run Dijkstra's shortest paths algorithm on the graph as there are no negative edge lengths.
This is a very fast algorithm, and overall this is faster than running Floyd-Warshall's algorithm for all pairs.
4. We have to make a final adjustment of removing p_u - p_v from all edges (u,v) once this is done.

"""
import dijkstra
import numpy as np


def outer_bf(A,N,graph):
	for i in range(1,N):
		A,carry_on = inner_bf(A,N,graph)
		if carry_on == False:
			break
	return A


def min_searcher(A,v,graph):
	edges = graph[v]
	candidates = []
	for e in edges:
		# the 0 index of e is the tail vertex, 1 index is the cost
		candidates.append(A[e[1]]+e[0])
	return min(candidates)


def subproblem_recurse(A,N,graph):
	B = list(A)
	for v in range(N):
		case1 = A[v]
		case2 = min_searcher(A, v, graph)
		B[v] = min(case1, case2)
	return B


def inner_bf(A,N,graph):
	B = subproblem_recurse(A,N,graph)
	if A == B:
		carry_on = False
	else:
		carry_on = True
	return B,carry_on


def neg_cyc_check(A,N,graph):
	B = subproblem_recurse(A, N,graph)
	neg_cyc = A != B
	return neg_cyc


def bellman_ford(graph,N):

	A = [np.inf for i in range(N+1)]
	A[N] = 0
	for i in range(N):
		#graph.append([N+1,i,0])
		graph[i].append([0,N])
		#graph[i+1].append([N+1,0])
	print 'graph enhanced with s'

	A = outer_bf(A,N,graph)
	neg_cyc = neg_cyc_check(A,N,graph)
	A.pop()
	return A,neg_cyc


def adjuster(graph,adjustments):
	for i in range(N):
		for v in graph[i]:
			v[0] += adjustments[i]-adjustments[v[1]]
	return graph


def johnson(graph_head,graph_tail,N):
	# pass bellman ford the graph as a list by head vertex.
	adjustments,neg_cyc = bellman_ford(graph_head,N)
	if neg_cyc:
		return 'NULL'

	graph_tail = adjuster(graph_tail,adjustments)
	print 'tail graph adjusted, running dijkstra'
	lengths = []
	for s in range(N):
		dij = dijkstra.dijkstra(graph_tail,s)
		#dij.__init__(graph_tail,s)
		
		sv = dij.main_loop_heap()
		# now readjust sv
		for i in range(len(sv)):
			sv[i] += adjustments[i]-adjustments[s]

		lengths.append(min(sv))
	return min(lengths)


if __name__ == '__main__':
	# run johnson on the 3 graphs provided by coursera

	# load in first set:
	g_file = "/Users/timscholtes/Documents/Code/git_repos/data/g3.txt"
	g_file = "Z:/GROUP/TIM/pp/data/g3.txt"
	#g_file = "Z:/GROUP/TIM/pp/data/johnson_demo.txt"

	with open(g_file) as file:
		for number, line in enumerate(file):
			if number == 0:
				N, M = line.split()
				N = int(N)
				M = int(M)
				graph_head = [[] for key in range(1, N+1)]
				graph_tail = [[] for key in range(1, N+1)]
			else:
				edge = ([int(i) for i in line.split()])
				# dijkstra is written to take the length first, then the vertex.
				graph_head[edge[1]-1].append([edge[2],edge[0]-1])
				graph_tail[edge[0]-1].append([edge[2],edge[1]-1])

	for v,u in enumerate(graph_head):
		u.append([0,v])
	for u,v in enumerate(graph_tail):
		v.append([0,u])

	A = johnson(graph_head,graph_tail,N)
	#adj,A = bellman_ford(graph_head,N)
	#print adj
	
	print A
	pass

