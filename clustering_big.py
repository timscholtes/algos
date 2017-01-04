import timeit
# we're going to create a union find class here
# This will work via rank, and path compression for speed.
# union choice is via a

class union_find:

	def __init__(self, vertices, n_vertices,nbits):

		# start out with each node as its own parent.
		self.vertices = vertices
		self.nbits = nbits
		self.ranks = {x:0 for x in vertices.keys()}
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
		while self.vertices[x] != x:
			tracker.append(x)
			x = self.vertices[x]
		for i in tracker:
			self.vertices[i] = x
		return x


	def union(self,p1,p2):

		self.k -= 1
		s1 = self.ranks[p1]
		s2 = self.ranks[p2]

		if s1 > s2:
			self.vertices[p2] = p1
		elif s1 < s2:
			self.vertices[p1] = p2
		elif s1 == s2:
			self.vertices[p1] = p2
			self.ranks[p2] += 1

		pass

	def bitswap(self, x, n):
		# convert to integer list
		digits = [int(i) for i in x]
		# swap it
		digits[n] = 1-digits[n]
		# convert back to str
		out = reduce((lambda x, y: x + y), [str(i) for i in digits])
		return out

	def bitswap2(self,x,n):
		#x = int(x,2)
		comp = int('0'*n+'1'+'0'*(self.nbits-n-1),2)
		return x ^ comp
		#return '{0:024b}'.format(x ^ comp)

	def combo_gen(self, v):
		combos = []
		for i in range(self.nbits):
			v = self.bitswap2(v, i)
			combos.append(v)
			if i < self.nbits-1:
				for j in range(i+1,self.nbits):
					v = self.bitswap2(v, j)
					combos.append(v)
					# need to change it back for next run
					v = self.bitswap2(v, j)
			v = self.bitswap2(v, i)

		return combos


	def merge(self):

		self.k = self.n_vertices

		# loop through each vertex
		counter = 0
		for v in self.vertices:
			# progress reporting:
			counter += 1
			if counter % 100 == 0:
				print counter / float(self.n_vertices)

			combos = self.combo_gen(v)
			# loop through prospective candidates which are close enough
			for u in combos:
				if u in self.vertices:
					p1 = self.find_slow(v)
					p2 = self.find_slow(u)
					if p1 != p2:
						self.union(p1,p2)

		for v in self.vertices:
			self.find_slow(v)
		for v in self.vertices:
			self.find_slow(v)

		vals = self.vertices.values()
		return self.k, len(set(vals))



#A_file = "/Users/timscholtes/Documents/Code/git_repos/data/clustering1.txt"
A_file = "Z:/GROUP/TIM/pp/data/clustering_big.txt"
vertices = dict()
with open(A_file) as file:
	for number, line in enumerate(file):
		if number == 0:
			N, nbits = (int(i) for i in line.split())
		else:
			# only add if it hasnt been added already
			key = reduce((lambda x,y: x + y), [str(i) for i in line.split()])
			key = int(key,2)
			#key = [int(i) for i in line.split()]
			if key not in vertices:
				vertices[key] = key
N = len(set(vertices.values()))


union_f = union_find(vertices, N, nbits)

"""
a = vertices.keys()[0]
a_s = '{0:024b}'.format(a)

print a,"",a_s
n = 10
combos = union_f.combo_gen(a)
for i in range(10):
	print combos[i],'{0:024b}'.format(combos[i])
"""

print union_f.merge()