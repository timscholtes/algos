
"""Here we're going to create a class which can analyse the shortest path from any vertex to any other vertex,
Using Dijkstra's algorithm. First we will do it in o(mn) time,
 then in another implementation using heaps, in O(logn) time"""
import heapq
import time


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


class dijkstra:

	def __init__(self,graph_file,start):
		# initialize some arrays:
		self.X = {start}
		self.graph = {}

		with open(graph_file) as file:
			for index, line in enumerate(file):
				heads = [i for i in line.split()]
				self.graph[int(heads[0])] = [list(map(int,i.split(',')))[::-1] for i in heads[1:]]
		self.N = len(self.graph)
		self.A = {n:0 for n in range(1,self.N+1)}
		pass

	def graph_inspect(self,K):
		for k in range(1,K+1):
			print k,self.graph[k]
		pass

	"""pick an edge (u,v) with u in X, v not in X, that minimizes: A[u] + l_uv"""
	def edge_picker(self):
		min_len = 1e8
		candidate = (0,0)
		for u in self.X:
			for v in self.graph[u]:
				if v[1] not in self.X:
					dist = self.A[u] + v[0]
					if dist < min_len:
						candidate = (u,v[1])
						min_len = dist
		self.X.add(candidate[1])
		self.A[candidate[1]] = min_len
		pass

	def heap_update(self,u):
		for v in self.graph[u[1]]:
			if v[1] not in self.X:
				if v[1] not in self.X and v[1] not in self.pq.entry_finder:
					self.pq.insert(v[1],u[0]+v[0])
				elif v[1] not in self.X and v[1] in self.pq.entry_finder:
					old_dist = self.pq.delete(v[1])
					new_dist = min(old_dist,u[0]+v[0])
					self.pq.insert(v[1],new_dist)
		pass

	def main_loop_heap(self):
		while len(self.X) < self.N:
			new_vertex = self.pq.pop()
			self.A[new_vertex[1]] = new_vertex[0]
			self.X.add(new_vertex[1])
			self.heap_update(new_vertex)
		print "Done"

		return self.A

	def main_loop(self):

		while len(self.X)<self.N:
			self.edge_picker()
		print "Done"

		return self.A


dij = dijkstra("/Users/timscholtes/Documents/Code/git_repos/data/shortest_path.txt",1)
dij.graph_inspect(100)
tic = time.clock()
A = dij.main_loop_heap()
toc = time.clock()
print 'heap: ', toc-tic

tic = time.clock()
A = dij.main_loop()
toc = time.clock()
print 'heap: ', toc-tic

