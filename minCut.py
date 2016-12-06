""" 
This code is designed to calculate the minimum cuts for an undirected graph
Input data is via an adjacency list.
This has first column as the vertex indices, 
with subsequent columns as the adjacent (i.e. connected) vertices.
This is implemented by running a random contraction algorithm.
"""
import random

class minCutter:

	def __init__(self,graph_file):
		self.graph = {}
		self.M = 0
		self.N = 0
		with open(graph_file) as file:
			for index, line in enumerate(file):
				numbers = [int(number) for number in line.split()]
				self.graph[numbers[0]] = numbers[1:]
				self.M += len(numbers[1:])
				self.N += 1


	def pick_rand_edge(self):
		m = random.randrange(self.M)
		for n in self.graph.keys():
			
			if(len(self.graph[n])<=m):
				m -= len(self.graph[n])
			else:
				return n,self.graph[n][m]


	def rand_contract(self):
		# first select a random edge. cannot do it from adjacency list, as we need parallel edges to affect the probability
		edge_to_cont = self.pick_rand_edge()

		tmp_m = len(self.graph[edge_to_cont[0]])+len(self.graph[edge_to_cont[1]])
		# remove references to the head in the tail - this is the edge we are contracting!
		self.graph[edge_to_cont[0]] = [k for k in self.graph[edge_to_cont[0]] if k != edge_to_cont[1]]
		# remove references to the tail in the head (these will become self loops)
		self.graph[edge_to_cont[1]] = [k for k in self.graph[edge_to_cont[1]] if k != edge_to_cont[0]]
		
		# reduce M:
		self.M -= tmp_m - len(self.graph[edge_to_cont[0]]) - len(self.graph[edge_to_cont[1]])
		# change all external refs to the head into refs to the tail
		# we can go through where these are by looking at the tail vertex adjacencies
		for l in self.graph[edge_to_cont[1]]:
			self.graph[l] = [k if k != edge_to_cont[1] else edge_to_cont[0] for k in self.graph[l]]


		# merge the two points on the graph
		self.graph[edge_to_cont[0]].extend(self.graph[edge_to_cont[1]])
		del self.graph[edge_to_cont[1]]


		pass


	def minCut(self):
		
		while self.N > 2:
			#print self.N
			self.rand_contract()
			self.N -= 1
		return len(self.graph[self.graph.keys()[0]])


def minCutMC(K):
	mc = minCutter('kargerMinCut.txt')
	N = mc.N
	min_cut = N
	for k in range(K):
		mc = minCutter('kargerMinCut.txt')
		min_cut_tmp = mc.minCut()
		print k,min_cut_tmp
		if min_cut_tmp < min_cut:
			min_cut = min_cut_tmp

	return min_cut

print minCutMC(500)