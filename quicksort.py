
def choosePivotFirst(A,l,r):
	return l

def choosePivotLast(A,l,r):
	return r

def choosePivotMedian(A,l,r):
	pass


def partition(A,l,r,p,p_val):

	# replace first element with pivot value
	if p != l:	
		A[p] = A[l]
		A[l] = p_val

	# sort into left and right
	i = l+1
	for j in range(l+1,r):
		if A[j] < p_val:
			tmp = A[j]
			A[j] = A[i]
			A[i] = tmp
			i += 1

	# replace i-1th with 1st
	tmp = A[l]
	A[l] = A[i-1]
	A[i-1] = tmp

	return A, i-1


def quickSort(A,l,r):

	# base case
	if r == l:
		return(A)

	p = choosePivotFirst(A,l,r)
	p_val = A[p]

	A, p = partition(A,l,r,p,p_val)
	
	A = quickSort(A,l,p) # work on left
	A = quickSort(A,p+1,r) # work on right

	return A


def quickSortCount(A,l,r,m):

	# base case
	if r == l:
		return(A)

	p = choosePivotFirst(A,l,r)
	p_val = A[p]

	m += r-l-1
	A, p = partition(A,l,r,p,p_val)
	
	print(m)
	A, m = quickSort(A,l,p,m) # work on left
	A, m = quickSort(A,p+1,r,m) # work on right

	return A, m


#################################


in_vec = [5,6,4,10,2,1,3,7,20]


A1 = quickSort(in_vec,0,len(in_vec))
print(A1)

A2 = quickSortCount(in_vec,0,len(in_vec),0)

