from collections import defaultdict
# the '2' versions are pure, they return the leader nodes for all vertices
# the base version simply upgrades counts of vertices, specifically for the exam q.

def DFS_loop2(grph,run_order,N):

	# initialise a boolean, false for all vertices, saying whether this vertex has been explored
	explored_bool = {key: False for key in grph.keys()}
	t = 0

	#initialise ft and leaders to zero
	ft = {key:0 for key in grph.keys()}
	leader = {key:0 for key in grph.keys()}

	# in the order of starting nodes specified by run_order, run DFS, and update ft and leader dicts.
	for i in run_order:
		ft, leader, explored_bool, t = DFS2(grph,i,ft,leader,explored_bool,t)

	return ft,leader


def DFS2(grph,v,ft,leader,explored_bool,t):
	# Check if the starting node v is explored.
	# If not, continue
	if not explored_bool[v]:
		S = [v]
		s = v

		while len(S)>0:
			# need to check there are outgoing edges!
			v = S[len(S)-1]             # take v as the last in S
			explored_bool[v] = True     # mark v as explored
			check = True
			k = 0
			# Loop through outgoing edges of v, (v,w)
			while check and k < len(grph[v]):
				w = grph[v][k]
				# If w is not yet explored, then append to S,
				# and we go back to first while loop to explore w's edges.
				# this is the nature of DFS!
				if not explored_bool[w]:
					S.append(w)
					check = False
				k += 1
			if check:
				v = S.pop()
				leader[v] = s # set leader node of v to s
				t += 1
				ft[v] = t

	return ft, leader, explored_bool, t


def kosaraju2(graph,N):

	""" Kosaraju's two pass algorithm:
	This algo finds all the SCC's in the directed graph, and returns the top 5 in terms of size.
	The edges dataset consists of a list of edges (u,v), with u being the tail and v the head vertices."""

	# create graph from edges
	#graph = defaultdict(list)
	graph_rev = {key:[] for key in graph.keys()}

	for k,vs in graph.items():
		for v in vs:
			graph_rev[v].append(k)

	print "read in"
	# run a DFS loop on G, in reverse fashion. Record finishing time.
	ft,leader = DFS_loop2(graph_rev,reversed(graph_rev.keys()),N)


	ft_order = sorted(ft.keys(), key=lambda k: ft[k])

	# run DFS loop on G, forward, using finishing time as loop sequence.
	ft,leader = DFS_loop2(graph,ft_order[::-1],N)

	return leader

if __name__ == '__main__':
	#print kosaraju("/Users/timscholtes/Documents/Code/git_repos/data/scc.txt",875714)
	graph = {1:[3], 2:[4], 3:[2],4:[]}
	print kosaraju2(graph,4)
