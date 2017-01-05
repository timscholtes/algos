

A_file = "/Users/timscholtes/Documents/Code/git_repos/data/mwis.txt"

weights = []
with open(A_file) as file:
	for line in file:
		weights.append(int(line))
N = weights.pop(0)


A = [0,weights[0]]

for i in range(1,N):
	A.append(max(A[i],A[i-1] + weights[i]))


# reconstruct:
S = []
i = N-1
print len(A)
while i > 2:

	if A[i+1] > A[i] + weights[i]:
		i -= 1
	else:
		S.append(i+1)
		i -= 2
S = set(S)
check = [1, 2, 3, 4, 17, 117, 517, 997]

bits = ''
for i in check:
	print i
	if i in S:
		bits = bits + '1'
	else:
		bits = bits + '0'

print bits


