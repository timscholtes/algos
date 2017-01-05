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
		self.bits = collections.defaultdict(list)

	def merge(self):
		# base case to recursion
		if len(self.weights_pq) == 2:
			return list(self.weights_pq)

		# find the two min size nodes:
		a = heappop(self.weights_pq)
		b = heappop(self.weights_pq)

		# create new combined node, with key of added weights, and value of a linked list
		# insert into the heap.
		ab = (a[0]+b[0],(a[1],b[1]))
		heappush(self.weights_pq,ab)
		# recurse
		self.merge()

	def unwrap(self,nested_list,val=0):
		print nested_list,type(nested_list[1]),val
		if isinstance(nested_list[1],int):
			self.bits[nested_list[1]].append(val)
			print self.bits
			return
		self.unwrap(nested_list[0],0)
		self.unwrap(nested_list[1],1)


huff = huffman([1,2,3,4],4)
huff.merge()
#print huff.weights_pq
weights_lst = huff.merge()

huff.unwrap(weights_lst)
print huff.bits
