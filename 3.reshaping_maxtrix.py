import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	matrix = np.array(a)

	rows=len(a)
	col=len(a[0])

	if((rows*col)==(new_shape[0]*new_shape[1])):

		reshaped_matrix= matrix.reshape(new_shape).tolist()

		return reshaped_matrix

	return []