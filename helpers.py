def square_matrix(n, placeholder=False):
	matrix = []
	for i in range(n):
		lista = [placeholder for i in range(1, n+1)]
		matrix.append(lista)
	return matrix

def gen_diagonal(diagonal, n, placeholder=False, element=True):
	if diagonal >= 2*n:
		return 'Diagonal parameter must be less than 2 times the size of the matrix'
	else:
		matrix = square_matrix(n, placeholder)

		for i in range(n):
			for j in range(n):
				if diagonal - 1 == i + j:
					matrix[i][j] = element
		return matrix



def diagonalize_array(array):

	n = int(len(array) ** 0.5)
	l = 0
	k = 1
	output = square_matrix(n, placeholder="")

	while k < 2*n:
		matrix = gen_diagonal(k, n, placeholder="", element="Diagonal")

		for i in range(n):
			for j in range(n):
				if matrix[i][j] == "Diagonal":
					output[i][j] = array[l]
					l += 1
		k += 1

	return twoD_to_linear(output)

def twoD_to_linear(array):
	output = []
	for lista in array:
		output = [*output, *lista]
	return output