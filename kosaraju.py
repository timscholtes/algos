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
	S = []
	S.append(v)
	s = v
	while len(S)>0:
		# need to check there are outgoing edges!
		v = S.pop()
		leader[s-1] += 1
		if not explored_bool[v]:
			explored_bool[v] = True
			for w in grph[v]:
				S.append(w)
		else:
			t += 1
			ft[v-1] = t
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
	print "finished first pass"
	ft_order = sorted(range(len(ft)), key=lambda k: ft[k])
	print ft_order[0:20]
	print ft_order[::-1][0:20]
	# run DFS loop on G, forward, using finishing time as loop sequence. Record leaders.
	# Within each segment of DFS (i.e. during DFS's exploration phase),
	# increment a count of vertices belonging to leader vertex
	#DFS_loop(graph,ft_stack)
	ft,leader = DFS_loop(graph,ft_order[::-1])
	leader.sort(reverse=True)
	return leader[0:4]

print kosaraju("scc.txt")