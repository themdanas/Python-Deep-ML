def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	row=len(matrix)
	col=len(matrix[0])

	result=[]
	
	for i in range(row):
		s_res=[]
		for j in range(col):
			newm=matrix[i][j]*scalar
			s_res.append(newm)
		result.append(s_res)

	return result