# SORT LIBRARY
# INSERTION-SORT
def insertion_sort(x):
	"""INSERTION SORT ALGORITHM
	:param x: List to be sort
	:return x: Sorted List
	"""
	for j in range(1, len(x)):
		key = x[j]
		# Insert x[j] into the sorted sequence x[1..j-1]
		i = j-1
		while (i >= 0) and (x[i] > key):
			x[i+1] = x[i]
			i = i-1
		x[i+1] = key
	return x