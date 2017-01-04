"""This function will return the number of t target values in the range
A = [-10000,10000] which have distinct numbers x and y which satisfy x + y = t.
We proceed by a hashing routine:
Insert A into hash table H
for each x in A
    lookup t-x !=x in H
"""

class intDict(object):

	def __init__(self,numBuckets):
		self.buckets=[]
		self.numBuckets = numBuckets
		for i in range(numBuckets):
			self.buckets.append([])

	def addEntry(self,value):
		hashBucket = self.buckets[value % self.numBuckets]
		for i in hashBucket:
			if i == value:
				return
		hashBucket.append(value)

	def checkValue(self,value):
		hashBucket = self.buckets[value % self.numBuckets]
		for i in hashBucket:
			if i == value:
				return True
		return False



def checker(t,values,h):
	for x in values:
		if t-x != x:
			if h.checkValue(t-x):
				return True
	return False


def doubleSummer(A):
	H = intDict(1299827)
	for a in A:
		H.addEntry(a)
	print "finished hashing"

	counter = 0
	for t in range(-10000,10001):
		if t % 100 == 0:
			print 100*(t+10000)/float(20000),"% done"

		if checker(t,A,H):

			counter += 1


	return counter

A_file = "/Users/timscholtes/Documents/Code/git_repos/data/doubleSum.txt"
A = []
with open(A_file) as file:
	for line in file:
		A.append(int(line))

print len(A)

print doubleSummer(A)
