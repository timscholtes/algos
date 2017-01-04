def checker(t,values,h):
	for x in values:
		y = t-x
		if y != x:
			if y in h:
				return True
	return False

def doubleSummer(A):
	H = {a:None for a in A}

	print "finished hashing"

	counter = 0
	for t in range(-10000 ,10001):
		if t % 100 == 0:
			print 100* (t + 10000) / float(20000), "% done"

		if checker(t, A, H):
			counter += 1

	return counter


A_file = "/Users/timscholtes/Documents/Code/git_repos/data/doubleSum.txt"
A = []
with open(A_file) as file:
	for line in file:
		A.append(int(line))

print len(A)

print doubleSummer(A)
