"""Here we're going to implement a nearest neighbour version of the travelling salesman problem.
The algo is as follows:
1. start at first city
2. Repeatedly visit the closest city the tour hasnt visited yet.
In case of a tie, go to the closest city with the lowest index.
3. Once every city has been visited exactly once, return to the first city."""

import numpy as np

def euclid_dist(a,b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)


def TSP_nn(cities,N):

	#cities is the set of unexplored cities
	start_loc = cities.pop(0) #- this is the start
	loc = start_loc
	print loc
	# Loop over unexplored cities. get min dist city.
	# could investigate not recalculating all new distances each time, depending on the distance just travelled?
	# The order of min distances might be unlikely to be radically changed

	travel_dist = 0

	while len(cities) > 0:
		print len(cities)
		# reset the rolling measures
		rollmin = np.inf
		rollindex = 0

		# loop through the remaining cities
		for i in xrange(len(cities)):
			x = euclid_dist(loc, cities[i])
			#dists.append(x) # maybe don't need this, but could be useful for optimisations
			if x < rollmin:
				rollmin = x
				rollindex = i

		travel_dist += rollmin**0.5
		loc = cities.pop(rollindex)

	travel_dist += euclid_dist(start_loc,loc)**0.5
	return travel_dist


if __name__ == "__main__":


	cities = []


	g_file = "/Users/timscholtes/Documents/Code/git_repos/data/nn.txt"

	with open(g_file) as file:
		for number, line in enumerate(file):
			if number == 0:
				N = int(line)
			else:
				out = [float(i) for i in line.split()]
				out.pop(0)
				cities.append(out)


print TSP_nn(cities,N)
