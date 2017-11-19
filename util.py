import numpy as np
from numpy.linalg import matrix_power

# Takes in probability matrix P and number of transition t
# Returns P^t
def transition_matrix_after_t(P, t):
	# P_t = P
	# for _ in range(t-1):
	# 	P_t = np.dot(P_t, P)

	# return P_t
	return matrix_power(P, t)

# Extracts row i from matrix P^t
# returns vector P^t_i
#def col_prob_vector(P_t, i):
#	return P_t[i,:]

# Compute probability from a community to all its adjacent vertices
# Returns vector P^t_C.
def community_to_adj(P_t, C):
	if C != []:
		N = len(P_t)
		P_t_C =	np.zeros(N)

		for j in range(N):
			total = 0 
			for i in C:
				total = total + P_t.item((i-1, j))
			P_t_C[j] = total / len(C) 
		return P_t_C
