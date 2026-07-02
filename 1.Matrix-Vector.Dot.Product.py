def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	a_row=len(a)
	a_col=len(a[0])

	b_row=len(b)
	

	result = []

	if(a_col == b_row):
		for i in range(a_row):
			dot = 0
			for j in range(b_row):
				dot += a[i][j]*b[j]
				

			result.append(dot)
			
		return result


	return -1