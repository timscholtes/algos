# Enter your code here. Read input from STDIN. Print output to STDOUT
#N,l = map(int,raw_input().split())
N,l = 100000,2
 
graph = {}
for i in xrange(l):
    a,b = map(int,raw_input().split())
    # Store a and b in an appropriate data structure
    graph.setdefault(a,[]).append(b)
    graph.setdefault(b,[]).append(a)

def BFS(graph,visited,v):
    counter = 0
    q = [v]
    visited[v] = True
    while len(q)>0:
        v = q.pop()
        counter += 1
        for w in graph[v]:
            if not visited[w]:
                q.insert(0,w)
                visited[w] = True
    return counter,visited


def index_of_first(dic):
    for i,v in dic.items():
        if not v:
            return i
    return None


def BFS_loop(graph):
    #visited = [False for n in range(N)]
    visited = {k:False for k in graph.keys()}
    start = index_of_first(visited)
    groups = []
    while start != None:
        counter,visited = BFS(graph,visited,start)
        groups.append(counter)
        start = index_of_first(visited)
    return groups


def n_pairs(groups):
    n = len(groups)
    counter = 0
    singles = N-len(graph)
    

    for i in range(n):
        counter = counter + groups[i]*singles # don't want to compute over mostly empty graph
        for j in range(i+1,n):
            counter = counter + groups[i]*groups[j]

    n_c_2 = singles * (singles-1) / 2
    counter = counter + n_c_2

    return counter

result = n_pairs(BFS_loop(graph))
    
# Compute the final result using the inputs from above

print result