""" This code aims to produce an algo which can solve a simple knapsack problem

The data provided is small enough to run the normal DP solution to the problem.
We don't need to reproduce the actual composition, simply the max value."""

import numpy
import heapq
import time

def knapsack(W,N,items):
	"""Calculates the optimum value of the knapsack problem

	Creates an auxillary array which will hold values of previously encountered subproblems
	This is available for constant time lookup

	Args:
		W: total weight capacity of knapsack
		N: number of items
		items: dictionary of items weight and value. Key is number n {0,1,2,3,...,N},
		 and value is tuple of (value,weight)

	Returns:
		total value of knapsack
		"""


	A = numpy.zeros((N+1,W+1),numpy.int)

	A[0,] = 0

	for i in range(1,N+1):
		for x in range(W+1):
		#	print A
			case1 = A[i-1,x]
			if x-items[i][1] < 0:
				case2 = case1
			else:
				case2 = A[i-1,x-items[i][1]]+items[i][0]

			A[i,x] = max(case1,case2)
	#print A
	return A[N,W]


#print knapsack(10,5,{i:(2,3) for i in range(1,6)})




A_file = "/Users/timscholtes/Documents/Code/git_repos/data/knapsack1.txt"


items = dict()
with open(A_file) as file:
	for number, line in enumerate(file):
		if number == 0:
			W,N = (int(i) for i in line.split())
		else:
			items[number] = [int(i) for i in line.split()]
#print items


#knapsack(W,N,items)

# --------------------------------------------------------------------------------

def knapsack2(W,N,items,min_wt):
	"""Calculates the optimum value of the knapsack problem, but for very large N,W

	This problem is infeasible using the normal method
	The space and time would make it too hard.
	So we reduce A to only include the slice of A[i,], A[i-1,] (we're not tracing back to find the actual solution)
	This reduces the space by a factor of 1000.
	But we still have 2e6 for the W:
		We can help reduce this by realising that we may look over A in the range 2,max(W).
		Here max(W is about 1e6) (half the size of the bag)
		min(W) is 8000, so we know that for x < 8000 the array will be all zeros
		does order of evaluation help? Put the items into a heap by weight, try pulling heaviest then by lightest



	Args:
		W: total weight capacity of knapsack
		N: number of items
		items: dictionary of items weight and value. Key is number n {0,1,2,3,...,N},
		 and value is tuple of (value,weight)

	Returns:
		total value of knapsack
		"""

	heap = []
	for k in items:
		heapq.heappush(heap,[-k[1],k[0]])

	#A = numpy.zeros((2,W+1-min_wt),numpy.int)
	A = numpy.zeros((2, W + 1), numpy.int)

	i = 0
	counter = 0

	while heap:

		counter += 1

		i = 1-i # i flips between 0 and 1, and we build the left and right cols of A iteratively

		item = heapq.heappop(heap)

		# reverse the item (so value is first)
		item = [item[1], -item[0]]
		print counter,item[1]
		#print 'value:',item[0],'weight:',item[1]

		# don't need to loop through all range(W+1)
		# we know we won't be in case2 for x remaining < item size, so why recurse?
		# Instead recurse in the opposite direction, until x == item size.

		#for x in range(W-min_wt,0,-1):
		for x in xrange(W, item[1], -1):

			case1 = A[1-i,x] # first time this is found, stop?
			case2 = A[1-i,x-item[1]]+item[0]

			A[i,x] = max(case1,case2)

	return A[i,W]

#print knapsack2(6,4,[[3,4], [2,3], [4,2],[4,3]],2)


def case_checker(A,item,W):

	for x in xrange(W, item[1]-1, -1):

		case1 = A[x]  # first time this is found, stop?
		case2 = A[x - item[1]] + item[0]
		if case2 > case1:
			A[x] = case2

		# not sur whwy the below doesnt return correct answer
		#Alternatively can maintain the locations of the differences in the vector A, and fill values between these marks
		#else:
			#print 'stopped at:',x,',wt:',item[1],',val:',item[0], ',swap index:',x-item[1],',cur val at swap:',A[x-item[1]],',swap:',item[0]
		#	return A

	return A

def knapsack3(W,items):

	heap = []
	for k in items: # order is priority then value (weight then val)
		heapq.heappush(heap,[k[1],k[0]])

	A = [0 for i in xrange(W+1)]

	counter = 0

	while heap:
		counter += 1
		print counter
		item = heapq.heappop(heap)
		# reverse the item (so value,weight)
		item = [item[1],item[0]]
		#print 'value:',item[0],'wt:',item[1]

		A = case_checker(A,item,W)

		#print A[9990:]

	return A.pop()



A_file = "/Users/timscholtes/Documents/Code/git_repos/data/knapsack2.txt"


items = []
min_wt = 1e6
with open(A_file) as file:
	for number, line in enumerate(file):
		if number == 0:
			W,N = (int(i) for i in line.split())
		else:
			X = [int(i) for i in line.split()]
			items.append(X)
			min_wt = min(min_wt,X[1])
# value in first, then wt

print knapsack3(W,items)
#print knapsack3(6,[[3,4], [2,3], [4,2],[4,3]])

