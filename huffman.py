__author__ = 'tim.scholtes'
from heapq import *
import collections
#import priority_queue
class huffman:

	def __init__(self,weights,N):
		weights = [(values,keys) for keys,values in enumerate(weights)]
		self.N = N
		self.weights_pq = []
		for i in weights:
			heappush(self.weights_pq,i)
		#self.bits = {i:[] for i in range(N)}
		self.bits = [0 for i in range(N)]
		self.counter = 0


	def merge(self):

		print len(self.weights_pq)
		# base case to recursion
		if len(self.weights_pq) == 2:
			out = list(self.weights_pq)
			out = (out[0][1],out[1][1])
			return out

		# find the two min size nodes:
		a = heappop(self.weights_pq)
		b = heappop(self.weights_pq)

		# create new combined node, with key of added weights, and value of a linked list
		# insert into the heap.
		ab = (a[0]+b[0],(a[1],b[1]))
		heappush(self.weights_pq,ab)
		# recurse
		self.merge()


	def merge2(self):

		while len(self.weights_pq) > 2:
			# find the two min size nodes:
			a = heappop(self.weights_pq)
			b = heappop(self.weights_pq)

			# create new combined node, with key of added weights, and value of a linked list
			# insert into the heap.
			ab = (a[0] + b[0], (a[1], b[1]))
			heappush(self.weights_pq, ab)

		out = list(self.weights_pq)
		out = (out[0][1], out[1][1])
		return out


	def unwrap(self,nested_list,val=[]):

		if isinstance(nested_list,int):
			self.bits[nested_list] = list(val)
			return

		val.append(0)
		self.unwrap(nested_list[0],val)

		val.pop()
		val.append(1)

		self.unwrap(nested_list[1],val)
		val.pop()


A_file = "/Users/timscholtes/Documents/Code/git_repos/data/huffman.txt"

weights = []
with open(A_file) as file:
	for line in file:
		weights.append(int(line))
N = weights.pop(0)


#weights = [1 for i in range(10)]
#N = len(weights)

huff = huffman(weights,N)


#print huff.weights_pq
weights_lst = huff.merge2()


huff.unwrap(weights_lst)

maxcount = 0
mincount = 100
for i in huff.bits:
	maxcount = max(maxcount, len(i))
	mincount = min(mincount, len(i))
print maxcount,mincount