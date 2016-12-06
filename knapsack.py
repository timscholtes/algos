# n is items left to choose from, S is space left

def Value(n,S,s_n,v_n):
	if n==0:
		return 0
	if s_n[n] > S:
		result = Value(n-1,S)
	else:
		result = max(v_n[n] + Value(n-1,S-s_n[n]))
