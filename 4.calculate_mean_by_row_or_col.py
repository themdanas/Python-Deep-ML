def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	row = len(matrix)
	col = len(matrix[0])

	total = 0
	means=[]

	if mode == "column":
		for j in range(col):
			for i in range(row):
				total+=matrix[i][j]
				
			mean=total/row
			means.append(mean)
			total=0
			
	else:
		for i in range(row):
			for j in range(col):
				total+=matrix[i][j]
				
			mean=total/col
			means.append(mean)
			total=0
			


	return means