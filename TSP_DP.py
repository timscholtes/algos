"""This is a dynamic programming algorithm for the travelling sales problem. 
It achieves an exponential runtime, substantially better than the brute force solution.
The rules are that for a fully connected non-directed graph, we mus return the minimum length
of a tour of all cities without visiting any of them more than once.

The solution for some mid-tour destination j proceeds by considering the iterative 
subproblem of ending up at an intermediate city k, and all of the sets of cities that could 
have been visited to arrive at k, excluding j, then adding on c_kj.

There are a lot of sub problems, O(n 2^n), and O(n) work per sub problem, but this is still better
than brute force which is O(n!), as the graph is fully connected.

Data is supplied in terms of a list of x,y coordinates of cities, distance being euclidean,
and assuming our salesman can fly.



"""
import collections
import itertools
import numpy as np

def defaulter():
	return [np.inf for i in range(N)]


def euclid_dist(a,b):
	return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5


def TSP(cities,N):

	# Initialise the memoisation array
	# This is going to be indexed by S,j, where S is the set of visited cities,
	# and j is the current city for consideration
	# As S is very large, I'm using a dictionary, where S is a tuple key.

	A = collections.defaultdict(defaulter)
	A[tuple([1])] = [np.inf for i in range(N)]
	A[tuple([1])][0] = 0

	# Generate the graph
	graph = []
	for i in range(N):
		graph.append([])
		for j in range(N):
			graph[i].append(euclid_dist(cities[i],cities[j]))


	for m in range(2,N+1):
		print m
		# cleanup A to make it smaller
		if m>3:
			for S in itertools.combinations(xrange(2,N+1),m-3):
				S2 = tuple([1] + list(S))
				A.pop(S2,None)


		# we're getting all combinations of length m, excluding 1,
		# as it's going to be in all of them (starting point)
		for S in itertools.combinations(xrange(2,N+1),m-1):
			# add in the 1
			S2 = tuple([1]+list(S))
			
			for j in S2[1:]:
				#leave out j from the set
				S2_j = tuple([k for k in S2 if k != j])
				# find the minimum way of getting to j, visiting all other cities
				# This is where the subproblems come in -
				# we have already calculated solutions for the smaller cases
				running_min = np.inf
				for k in S2_j:
					running_min = min(running_min,A[S2_j][k-1]+graph[k-1][j-1])
					#out.append(A[S2_j][k-1]+graph[k-1][j-1])
				A[S2][j-1] = running_min

	# Finally, we need to make it into a round trip tour, so looping through all j cities except 0,
	# find the route with the min distance once you include the final trip back to 0

	final = []
	key = tuple(range(1, N + 1))
	ult_combo = A[key]
	for j in range(2,N+1):
		print j
		final.append(ult_combo[j-1]+graph[j-1][0])

	return min(final)



if __name__ == "__main__":
	#import matplotlib.pyplot
	import time

	cities = []
	x = []
	y = []

	#g_file = "Z:/GROUP/TIM/pp/data/tsp.txt"

	g_file = "/Users/timscholtes/Documents/Code/git_repos/data/tsp.txt"

	with open(g_file) as file:
		for number, line in enumerate(file):
			if number == 0:
				N = int(line)
			else:
				out = [float(i) for i in line.split()]
				cities.append(out)
				x.append(out[0])
				y.append(out[1])



	start_time = time.time()
	print TSP(cities,N)
	end_time = time.time()

	print end_time - start_time
	#combo = itertools.izip(xrange(1,2),itertools.combinations(xrange(2,N+1),3-1))

#print list(itertools.combinations(range(15),3))
#matplotlib.pyplot.scatter(x,y)
#matplotlib.pyplot.show()
