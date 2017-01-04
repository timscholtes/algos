"""This program maintains the median of a set of numbers as they arrive.
It uses a two heap data structure, with each heap capturing the lower half
and upper half respectively.
The function returns all of the medians as a list,
assuming the input arrives as a stream of numbers."""



import heapq


class medianMaintainer:

	def __init__(self,stream_file):
		self.stream=[]
		with open(stream_file) as file:
			for line in file:
				self.stream.append(int(line))
		self.N = len(self.stream)

		self.low_heap  = []
		self.high_heap = []
		heapq.heapify(self.high_heap)
		heapq.heapify(self.low_heap)
		self.medians = []

	def mainLoop(self):
		for i in range(self.N):
		#for i in range(10):
			#print self.stream[i]
			if i == 0:
				heapq.heappush(self.low_heap,-self.stream[i])
			elif self.stream[i] <= -self.low_heap[0]:
				heapq.heappush(self.low_heap, -self.stream[i])
			elif self.stream[i] > -self.low_heap[0]:
				heapq.heappush(self.high_heap,self.stream[i])


			#print "high",self.high_heap
			#print "low",self.low_heap
			if len(self.low_heap) > len(self.high_heap)+1:
				#print "shifting from low to high"
				x = heapq.heappop(self.low_heap)
				heapq.heappush(self.high_heap,-x)
			if len(self.high_heap) > len(self.low_heap):
				#print "shifting from high to low"
				x = heapq.heappop(self.high_heap)
				heapq.heappush(self.low_heap, -x)
			self.medians.append(-self.low_heap[0])

	pass



mm = medianMaintainer("/Users/timscholtes/Documents/Code/git_repos/data/median_maintanence.txt")
#mm = medianMaintainer("/Users/timscholtes/Documents/Code/git_repos/data/test.txt")
mm.mainLoop()
print sum(mm.medians) %10000


