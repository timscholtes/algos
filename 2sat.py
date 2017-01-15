""" THis algorithm is going to take a set of or statemtns in the form ('X_i or x_j) where the ' denotes not,
and can be on either variable, both or neither.
The task is to determine if there is a solution to the set of statements, in the form of
setting the x's to either true or false.

We proceed by creating a graph, where each variable is represented by 2 vertices, 1 for
itself and another for its negation. There are 2 directed edges for each:
x_i or x_j => (x_i' -> x_j), (x_j' -> x_i)
If an SCC contains both a variable and its negation, then there is no feasible solution.
"""

import kosaraju2 as ks

def two_sat(pairs,N):


	graph = {key:[] for key in range(-N,N+1)}
	del graph[0]

	for p in pairs:
		# x_i or x_j => (x_i' -> x_j), (x_j' -> x_i)
		graph[p[0] * -1].append(p[1])
		graph[p[1] * -1].append(p[0])

	SCCs = ks.kosaraju2(graph,N)

	for i in xrange(1,N+1):
		l1 = SCCs[i]
		l2 = SCCs[-i]
		if l1==l2:
			return False
	return True


if __name__ == '__main__':

	pairs_file = "/Users/timscholtes/Documents/Code/git_repos/data/2sat6.txt"

	pairs = []
	with open(pairs_file) as file:
		for number, line in enumerate(file):
			if number == 0:
				print line
				N = int(line)
			else:
				X = [int(i) for i in line.split()]
				pairs.append(X)

	print two_sat(pairs,N)

