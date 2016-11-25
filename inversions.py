import math

def merge(B,C):
    n = len(B)+len(C)
    D = []
    i = 0
    j = 0
    for k in range(n):
        if i < len(B) and (j >= len(C) or B[i] < C[j]):
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
    return (D)

def mergeSort(A):

    N = len(A)

    if N == 1:
        return A

    if N == 2:
        return merge([A[0]],[A[1]])
    else:

        split_len = math.floor(N / 2)

        B = A[:split_len]
        C = A[split_len:]

        out = merge(mergeSort(B),mergeSort(C))

    return out


#print(mergeSort([1,4,3,2,7,5,9,8,10]))


def merge2(B,C):
    left_inv = B[1]
    right_inv = C[1]
    B = B[0]
    C = C[0]
    n = len(B)+len(C)
    D = []
    i = 0
    j = 0
    inversions = left_inv + right_inv
    for k in range(n):
        if i < len(B) and (j >= len(C) or B[i] < C[j]):
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1
            inversions += len(B)-i
    return (D,inversions)


def inversionCount(A,inversions):
    N = len(A)

    if N == 1:
        return (A,0)

    if N == 2:
        return merge2(([A[0]], 0), ([A[1]], 0))
    else:

        split_len = math.floor(N / 2)

        B = A[:split_len]
        C = A[split_len:]

        out = merge2(inversionCount(B,inversions),inversionCount(C,inversions))

    return out

#print(inversionCount([1,4,3,2,7,5,9,8,10],0))

text_file = open("inversions.txt", "r")
lines = text_file.read().split("\n")
lines = [int(x) for x in lines]
#print(lines[1:100])
print(inversionCount(lines,0)[1])