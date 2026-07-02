import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T = np.linalg.inv(T)
	t_col=len(T[0])
	A_row=len(A)
	A_col=len(A[0])
	S_row=len(S)
	if(np.linalg.det(T)!=0 and np.linalg.det(S)!=0):
		transformed_matrix=np.linalg.multi_dot([T,A,S])

	else:
		return -1
		
	return transformed_matrix