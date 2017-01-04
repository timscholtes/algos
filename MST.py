
import heapq


class PriorityQueue(object):
	"""Priority queue based on heap, capable of inserting a new node with
	desired priority, updating the priority of an existing node and deleting
	an abitrary node while keeping invariant"""

	def __init__(self, heap=[]):
		"""if 'heap' is not empty, make sure it's heapified"""

		heapq.heapify(heap)
		self.heap = heap
		self.entry_finder = dict({i[-1]: i for i in heap})
		self.REMOVED = '<remove_marker>'

	def insert(self, node, priority=0):
		"""'entry_finder' bookkeeps all valid entries, which are bonded in
		'heap'. Changing an entry in either leads to changes in both."""

		if node in self.entry_finder:
			self.delete(node)
		entry = [priority, node]
		self.entry_finder[node] = entry
		heapq.heappush(self.heap, entry)

	def delete(self, node):
		"""Instead of breaking invariant by direct removal of an entry, mark
		the entry as "REMOVED" in 'heap' and remove it from 'entry_finder'.
		Logic in 'pop()' properly takes care of the deleted nodes."""

		entry = self.entry_finder.pop(node)
		entry[-1] = self.REMOVED
		return entry[0]

	def pop(self):
		"""Any popped node marked by "REMOVED" does not return, the deleted
		nodes might be popped or still in heap, either case is fine."""

		while self.heap:
			priority, node = heapq.heappop(self.heap)
			if node is not self.REMOVED:
				del self.entry_finder[node]
				return priority, node
		raise KeyError('pop from an empty priority queue')


#going to implement Prims MST algo, using a heap (which supports deletions)
#  Initialize X = {s} [s in V chosen arbitrarily]
# - T = 0 [invariant: X = vertices spanned by tree-so-far T ]
# - WhileX !=V
# - Let w = (u,v) be the cheapest edge of G with u in X, v !in X. -Add e toT,add v toX.

# data format:
#[number_of_nodes] [number_of_edges]
#[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
#[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
#etc



#going to do repeated lookups of source node, so ought to put into a dictionary.

A_file = "/Users/timscholtes/Documents/Code/git_repos/data/MST_edges.txt"

with open(A_file) as file:
	for number, line in enumerate(file):
		if number == 0:
			N,M = line.split()
			N = int(N)
			M = int(M)
			A = {key: [] for key in range(1, N+1)}
		else:
			edge = ([int(i) for i in line.split()])
			A[edge[0]].append((edge[1:])[::-1])
			A[edge[1]].append(([edge[0],edge[2]])[::-1])

print A[1]

class prim_MST:

	def __init__(self,graph,N,M,start):
		self.graph = graph
		self.N = N
		self.M = M

		# initialise X which is the vertices in the MST
		self.X = {start}

		#initialise T which is edges (costs) in MST
		self.T = []

		# make the heap structure, initialised for graph[start]
		self.unexplored = []
		for v in self.graph[start]:
			heapq.heappush(self.unexplored,v)
		self.pq = PriorityQueue(self.unexplored)



	"""pick an edge (u,v) with u in X, v not in X, that minimizes: l_uv"""
	def edge_picker(self):
		min_len = 1e8
		candidate = (0,0)
		for u in self.X:
			for v in self.graph[u]:
				if v[1] not in self.X:
					dist = v[0]
					if dist < min_len:
						candidate = (u,v[1])
						min_len = dist
		print "adding (u,v):", candidate,"cost = ",dist
		self.X.add(candidate[1])
		self.T.append(min_len)
		pass

	def heap_update(self,u):
		for v in self.graph[u[1]]:
			if v[1] not in self.X:
				if v[1] not in self.pq.entry_finder:
					self.pq.insert(v[1],v[0])
				else:
					old_dist = self.pq.delete(v[1])
					new_dist = min(old_dist,v[0])
					self.pq.insert(v[1],new_dist)
		pass

	def main_loop_heap(self):
		while len(self.X) < self.N:
			new_vertex = self.pq.pop()
			self.X.add(new_vertex[1])
			self.T.append(new_vertex[0])
			self.heap_update(new_vertex)
		print "Done"

	def main_loop_slow(self):
		while len(self.X) < self.N:
			self.edge_picker()
		print "done"


prim = prim_MST(A,N,M,1)

prim.main_loop_heap()
print sum(prim.T)




