# we're going to create a union find class here
# This will work via rank, and path compression for speed.
# union choice is via a

class union_find:

	def __init__(self, edges, edge_costs, n_vertices):

		# start out with each node as its own parent.
		self.edges = edges
		self.edge_costs = edge_costs
		self.parents = range( n_vertices)
		self.ranks = [0 for i in range(n_vertices)]
		self.n_vertices = n_vertices
		pass

	def find(self, x):

		# using recursion here. Could maintain a list of traversed nodes if this proves too memory intensive?
		# terminate if at root
		if self.parents[x] != x:
			self.parents[x] = self.find(self.parents[x])
		# this line applies path compression and travels further up to the root.
		return x


	def find_slow(self, x):
		tracker = []
		while self.parents[x] != x:
			tracker.append(x)
			#print "recursing",self.k
			x = self.parents[x]
		for i in tracker:
			self.parents[i] = x
		return x


	def union(self,p1,p2):

		self.k -= 1

		s1 = self.ranks[p1]
		s2 = self.ranks[p2]

		if s1 > s2:
			self.parents[p2] = p1
			#for i in range(self.n_vertices):
			#	self.find_slow(i)
		elif s1 < s2:
			self.parents[p1] = p2
			#for i in range(self.n_vertices):
			#	self.find_slow(i)
		elif s1 == s2:
			self.parents[p1] = p2
			self.ranks[p2] += 1
			#for i in range(self.n_vertices):
			#	self.find_slow(i)
		pass


	def merge(self):
		# sort the edges
		# the loop through them, removing edges as they are merged.
		self.sorted_edge_costs = sorted(range(len(self.edge_costs)), key=lambda k: self.edge_costs[k])

		self.k = self.n_vertices
		consider = 0
		while self.k > 4:
			consider += 1
			index = self.sorted_edge_costs.pop(0)
			edge2contract = self.edges[index]

			p1 = self.find_slow(edge2contract[0])
			p2 = self.find_slow(edge2contract[1])

			if p1 != p2:
				self.union(p1,p2)
		print consider,p1,p2,set(self.parents)

		# now were done with the main loop, we need to carry on eliminating edges which are no separated
		# This means
		index = self.sorted_edge_costs.pop(0)
		edge2contract = self.edges[index]

		p1 = self.find_slow(edge2contract[0])
		p2 = self.find_slow(edge2contract[1])

		while p1 == p2:
			consider += 1
			index = self.sorted_edge_costs.pop(0)
			edge2contract = self.edges[index]

			p1 = self.find_slow(edge2contract[0])
			p2 = self.find_slow(edge2contract[1])

		print edge2contract,p1,p2
		print consider


		return self.edge_costs[index]



#A_file = "/Users/timscholtes/Documents/Code/git_repos/data/clustering1.txt"
A_file = "Z:/GROUP/TIM/pp/data/clustering1.txt"

edge_uv = []
edge_costs = []
with open(A_file) as file:
	for number, line in enumerate(file):
		if number == 0:
			N = int(line)
		else:
			edge_info = ([int(i) for i in line.split()])
			edge_uv.append([edge_info[0]-1,edge_info[1]-1])
			edge_costs.append(edge_info[2])

union_f = union_find(edge_uv,edge_costs,N)

print union_f.merge()
roots = [union_f.find(i) for i in union_f.parents]
print len(set(roots))