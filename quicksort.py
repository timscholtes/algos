import math
import numpy

def choosePivotFirst(A,l,r):
    return l


def choosePivotLast(A,l,r):
    return r-1


def choosePivotMedian(A,l,r):

    mid = int(math.ceil((r+l-1)/2))
    ordered = numpy.argsort([A[l],A[mid],A[r-1]])
    out = [l,mid,r-1][ordered[1]]
    return out


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
    if r-1 == l:
        return(A)

    p = choosePivotMedian(A,l,r)
    p_val = A[p]

    A, divider = partition(A,l,r,p,p_val)

    A = quickSort(A,l,divider) # work on left
    A = quickSort(A,divider+1,r) # work on right

    return A


def quickSortCount(A,l,r,m):
    # base case
    if r == l+1 or r == l:
        print("done")
        return A, m

    p = choosePivotMedian(A,l,r)
    p_val = A[p]
    print(l,r,p, p_val)

    m += r-l-1
    A, divider = partition(A,l,r,p,p_val)
    A, m = quickSortCount(A,l,divider,m) # work on left
    A, m = quickSortCount(A,divider+1,r,m) # work on right

    return A, m


#################################


text_file = open("QuickSort.txt", "r")
lines = text_file.read().split("\n")
in_vec = [int(x) for x in lines]
#in_vec = range(100)


in_vec, m_final = quickSortCount(in_vec,0,len(in_vec),0)
#in_vec, m_final = quickSortCount(in_vec,0,1,0)

print(m_final)
#


#162085
#164123
#159894
#138382