from PIL import Image
import os, shutil

# ---------- Matrixes
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

# ---------- os, shutil
def verify_path(directory):
	''' Verify if some provided path exists, if not, it is created '''
	if not directory: 
	        directory='tmp'
	        try:
		        shutil.rmtree(directory)
	        except:
	        	os.mkdir(directory)
	else:
	    try:
	        shutil.rmtree(directory)
	        os.mkdir(directory)
	    except:
	        os.mkdir(directory)
	return directory

# ---------- PIL
def colorbar(image, longitude):
    ''' Returns a resized bar of longitude 1 x n from a chromatic bar file '''
    return Image.open(image).resize((longitude, 1))

def pixel_resize(image):
    ''' Resize an image to 1x1 '''
    return Image.open(image).resize((1, 1))