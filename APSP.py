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


def outer_bf(A,N):
	for i in range(1,N):
		A,carry_on = inner_bf(A,N)
		if carry_on == False:
			break
	return A


def min_searcher(A,v,graph):
	edges = graph[v]
	candidates = []
	for e in edges:
		# the 0 index of e is the tail vertex, 1 index is the cost
		candidates.append(A[e[0]]+e[1])
	return min(candidates)


def subproblem_recurse(A,N):
	B = list(A)
	for v in range(N + 1):
		case1 = A[v]
		case2 = min_searcher(A, graph[v])
		B[v] = min(case1, case2)
	return B


def inner_bf(A,N):
	B = subproblem_recurse(A,N)
	if A == B:
		carry_on = False
	else:
		carry_on = True
	return B,carry_on


def neg_cyc_check(A,N):
	B = subproblem_recurse(A, N)
	neg_cyc = A != B
	return neg_cyc


def bellman_ford(graph,N):

	A = [np.inf for i in range(N+1)]
	A[len(N)+1] = 0
	for i in range(N):
		edges.append([N+1,i,0])

	A = outer_bf(A,N)
	neg_cyc = neg_cyc_check(A,N)
	A.pop()
	return A,neg_cyc

def adjuster(graph,adjustments):
	for i in range(N):
		graph[i][2] += adjustments[i]
	return graph


def johnson(G_N):
	# pass bellman ford the graph as a list by head vertex.
	adjustments,neg_cyc = bellman_ford(graph_head,N)
	if neg_cyc:
		return 'NULL'

	graph_tail = adjuster(graph_tail,adjustments)
	lengths = []
	for s in range(N):
		dij = dijkstra.dijkstra(graph_tail,s)
		lengths.append(dij.main_loop_heap())
	return min(lengths)


if __name__ == '__main__':
	# run johnson on the 3 graphs provided by coursera
	pass

