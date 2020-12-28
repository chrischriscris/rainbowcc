import os
import shutil
from pprint import pprint
from PIL import Image



# Matrix implementations
def mmatrix(m, n, placeholder=False):
	'''Returns an m x n matrix'''
	matrix = []
	for i in range(m):
		lista = [placeholder for i in range(0, n)]
		matrix.append(lista)
	return matrix

def gen_diagonal(diagonal, m, n, placeholder=False, element=True):
	if diagonal >= m+n:
		return 'Diagonal parameter must be less than m + n.'
	else:
		matrix = mmatrix(m, n, placeholder)

		for i in range(m):
			for j in range(n):
				if diagonal-1 == i+j:
					matrix[i][j] = element
		return matrix

def twoD_to_linear(array):
	output = []
	for lista in array:
		output = [*output, *lista]
	return output

def diagonalize_array(m, n, array):
	l = 0
	k = 1
	output = mmatrix(m, n, placeholder="")

	if len(array) != m*n:
		return f"{m}x{n} is not a valid size for your matrix."

	while k < m+n:
		matrix = gen_diagonal(k, m, n, placeholder="", element="Diagonal")

		for i in range(m):
			for j in range(n):
				if matrix[i][j] == "Diagonal":
					output[i][j] = array[l]
					l += 1
		k += 1

	return twoD_to_linear(output)



# os, shutil implementation
def verify_path(directory):
	''' Verify if some provided path exists, if not, it is created '''
	try:
		shutil.rmtree(directory)
		os.mkdir(directory)
	except:
		os.mkdir(directory)
	return directory



# PIL implementations
def colorbar(image, longitude):
    ''' Returns a resized bar of longitude 1 x n from a chromatic bar file '''
    return Image.open(image).resize((longitude, 1))
def pixel_resize(image):
    ''' Resize an image to 1x1 '''
    return Image.open(image).resize((1, 1))

