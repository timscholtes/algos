import math

def choosePivotFirst(A,l,r):
	return l

def choosePivotLast(A,l,r):
	return r-1

def choosePivotMedian(A,l,r):
	l_val = A[l]
	r_val = A[r-1]
	mid = A[int(math.ceil((r-l-1)/2))]
	sorted_vals = sorted([l_val,r_val,mid])
	return sorted_vals[1]


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

	p = choosePivotMedian(A,l,r)
	p_val = A[p]

	A, p = partition(A,l,r,p,p_val)
	
	A = quickSort(A,l,p) # work on left
	A = quickSort(A,p+1,r) # work on right

	return A


def quickSortCount(A,l,r,m):

	# base case
	if r == l:
		return A, m

	p = choosePivotMedian(A,l,r)
	p_val = A[p]

	m += r-l-1
	A, p = partition(A,l,r,p,p_val)
	
	A, m = quickSortCount(A,l,p,m) # work on left
	A, m = quickSortCount(A,p+1,r,m) # work on right

	return A, m


#################################


text_file = open("QuickSort.txt", "r")
lines = text_file.read().split("\n")
in_vec = [int(x) for x in lines]

#in_vec = [1,2,3,4,0]

A1 = quickSort(in_vec,0,5)
print(A1)


A2, m_final = quickSortCount(in_vec,0,len(in_vec)-1,0)
#print(A2)
