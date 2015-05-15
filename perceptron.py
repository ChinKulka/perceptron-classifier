"""
Implementation of Perceptron algorithm on MNIST dataset. 
"""

import numpy as np


def dot_prod(v1,v2):
	'''
	Returns projection of v1 on v2. 
	'''
	assert v1.size == v2.size, "vectors of different sizes"
	
	# Return scalar value of the dot product
	n = v1.size 
	dp = 0

	for i in xrange(n): 
		dp = dp + (v1[i] * v2[i])
	return dp  

def perceptron(data, labels, n_passes):
	'''
	Returns data matrix of weight vectors, where the last column is 
	the respective counts used for voted/averaged classification.  
	'''
	# Initialization step 
	w = np.zeros(data[0].size)
	m = 0
	c = 1
	n = labels.size
	w_vectors = [w]
	c_vectors = [1]

	# Iteration step. 
	for i in xrange(n):
		if (labels[i] * dot_prod(w,data[i])) <= 0:
			w = w + (labels[i] * data[i])
			w_vectors.append(w)
			c_vectors.append(c)
			m += 1 
		else: 
			c_vectors[m] += 1

	return np.insert(w_vectors,(data[i].size), c_vectors, axis=1)

def percep_orig_clf(weight_mat, data): 
	'''
	Returns prediction vector for input data, containing either 1 or -1. 
	'''
	# Take the last row from the weight matrix
	x, y = weight_mat.shape
	w = weight_mat[x-1][:-1]

	# Classification rule using dot product
	n, d = data.shape
	pred = []

	for i in xrange(n):
		if dot_prod(w,data[i]) > 0:
			pred.append(1)
		else:
			pred.append(-1)
	
	return np.array(pred)

def voted_percep_clf(weight_mat, data):
	'''
	Returns prediction vector using voted classification rule
	'''

def avg_percep_clf(weight_mat, data):
	'''
	Returns prediction vector using averaged classification rule
	'''

def main():
	# Parse input 
	train = np.genfromtxt("toy_data/toy_train.txt")
	test = np.genfromtxt("toy_data/toy_test.txt")

	# Separate data from labels
	train_labels = train[:,2]
	train_data = train[:,:-1]
	test_labels = test[:,2]
	test_data = test[:,:-1]


	wm = perceptron(train_data,train_labels,1)
	print percep_orig_clf(wm,test_data)

if __name__ == '__main__':
	main()