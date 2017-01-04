from collections import defaultdict


def DFS_loop(grph,run_order):

	# initialise a boolean, false for all vertices, saying whether this vertex has been explored
	explored_bool = {key: False for key in grph.keys()}
	t = 0
	ft = [0 for key in range(1,875715)]
	leader  = [0 for key in range(1,875715)]
	for i in run_order:
		ft, leader, explored_bool, t = DFS(grph,i,ft,leader,explored_bool,t)

	return ft,leader


def DFS(grph,v,ft,leader,explored_bool,t):
	if not explored_bool[v]:
		S = []
		S.append(v)
		s = v
		while len(S)>0:
			# need to check there are outgoing edges!
			v = S[len(S)-1]
			explored_bool[v] = True
			check = True
			k = 0
			while check and k < len(grph[v]):
				w = grph[v][k]
				if not explored_bool[w]:
					S.append(w)
					check = False
				k += 1
			if check:
				v = S.pop()
				leader[s - 1] += 1
				t += 1
				ft[v - 1] = t

	return ft, leader, explored_bool, t


def kosaraju(graph_file):

	""" Kosaraju's two pass algorithm:
	This algo finds all the SCC's in the directed graph, and returns the top 5 in terms of size.
	The edges dataset consists of a list of edges (u,v), with u being the tail and v the head vertices."""

	# create graph from edges
	#graph = defaultdict(list)
	graph = {key:[] for key in range(1,875715)}
	graph_rev = {key:[] for key in range(1,875715)}

	with open(graph_file) as file:
		for line in file:
			line = [int(number) for number in line.split()]
			graph[line[0]].append(line[1])
			graph_rev[line[1]].append(line[0])

	print "read in"
	# run a DFS loop on G, in reverse fashion. Record finishing time.
	ft,leader = DFS_loop(graph_rev,reversed(graph_rev.keys()))

	ft_order = sorted(range(len(ft)), key=lambda k: ft[k])
	ft_order = [k+1 for k in ft_order]

	# run DFS loop on G, forward, using finishing time as loop sequence.
	ft,leader = DFS_loop(graph,ft_order[::-1])

	leader.sort(reverse=True)
	return leader[0:5]

print kosaraju("/Users/timscholtes/Documents/Code/git_repos/data/scc.txt")
