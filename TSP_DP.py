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
import itertools
import collections
import numpy as np

def defaulter():
	return [np.inf for i in range(N)]



def TSP(cities,N):

	A = collections.defaultdict(defaulter)
	A[1] = [0 for i in range(N)]

	
	for m in range(2,N+1):
		print m

		for S in itertools.combinations(xrange(2,N+1),3-1):
			S2= [1]+list(S)
			
			for j in S2[1:]:
				x = list(A[S2])
				out = []
				S2_j = [k for k in S2 if k != j]
				for k in S2_j:
					out.append(A[S2_j][k-1]+graph[k-1][j-1])
				x[j-1] = min(out)
				A[S2] = x

	final = []
	for j in range(2,N+1):
		final.append(A[range(1,N+1)][j]+graph[j-1,0])

	return min(final)



if __name__ == "__main__":
	#import matplotlib.pyplot

	cities = []
	x = []
	y = []

	g_file = "Z:/GROUP/TIM/pp/data/tsp.txt"
	#g_file = "Z:/GROUP/TIM/pp/data/johnson_demo.txt"

	with open(g_file) as file:
		for number, line in enumerate(file):
			if number == 0:
				N = int(line)
			else:
				out = [float(i) for i in line.split()]
				cities.append(out)
				x.append(out[0])
				y.append(out[1])

	graph = []

	TSP(cities,4)
	#combo = itertools.izip(xrange(1,2),itertools.combinations(xrange(2,N+1),3-1))

#print list(itertools.combinations(range(15),3))
#matplotlib.pyplot.scatter(x,y)
#matplotlib.pyplot.show()
	