

#A_file = "/Users/timscholtes/Documents/Code/git_repos/data/mwis.txt"
A_file = "Z:/GROUP/TIM/pp/data/mwis.txt"

weights = []
with open(A_file) as file:
	for line in file:
		weights.append(int(line))
N = weights.pop(0)

#weights = [2,3,87,2,3,5,1,3]
#N = len(weights)


A = [0,weights[0]]
#print 'weights:',weights
for i in range(1,N):

	A.append(max(A[i],A[i-1] + weights[i]))

#print 'A:',A
#print 'N:',N
# reconstruct:
S = []
i = N-1
#print 'len(A):',len(A)
while i >= 0:
#	print i, A[i+1],A[i],weights[i]
	if A[i] > A[i-1] + weights[i]:
		i -= 1
	else:
		S.append(i+1)
		print 'accepted:',weights[i],'at pos',i+1
		i -= 2
S = set(S)
check = [1, 2, 3, 4, 17, 117, 517, 997]

bits = ''
for i in check:
#	print i
	if i in S:
		bits = bits + '1'
	else:
		bits = bits + '0'

#print S
print bits


