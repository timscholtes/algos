
A_file = "/Users/timscholtes/Documents/Code/git_repos/data/jobs.txt"
A = []
with open(A_file) as file:
	for index, line in enumerate(file):
		if index == 0:
			N = int(line)
		else:
			A.append([int(number) for number in line.split()])


def scheduler(wl):

	for i in xrange(len(wl)):
		wl[i].append(wl[i][0] - wl[i][1])

	wl.sort(key=lambda x: (x[2], x[0]), reverse=True)

	# now we have the schedule, we need to calculate the weighted sum of completion times.
	# the completion time is the running sum of the length
	# The weighted sum is the weight times the completion time.
	# For ties in the diff, we should use the version with the higher weight

	cmpl_t = 0
	wt_sum = 0
	for k in range(N):
		cmpl_t += wl[k][1]
		wt_sum += cmpl_t * wl[k][0]

	return wt_sum


def scheduler2(wl):

	for i in xrange(len(wl)):
		wl[i].append(wl[i][0] / float(wl[i][1]))

	wl.sort(key=lambda x: (x[2], x[0]), reverse=True)
	print wl[:20]
	# now we have the schedule, we need to calculate the weighted sum of completion times.
	# the completion time is the running sum of the length
	# The weighted sum is the weight times the completion time.
	# For ties in the diff, we should use the version with the higher weight

	cmpl_t = 0
	wt_sum = 0
	for k in range(N):
		cmpl_t += wl[k][1]
		wt_sum += cmpl_t * wl[k][0]

	return wt_sum



#print scheduler(A)
print scheduler2(A)



