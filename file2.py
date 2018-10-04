#!/bin/python3

def simple_array_sum(ar):
	"""
	Takes an 1D array (all elements are must be numbers) and sum them all.
	Example:
		input [1,2,3]
		output 1+2+3 = 6
	"""
	val = 0
	for n in range(0, own_len(ar)):
		val += ar[n-1]
	return val 

def own_len(array):
	"""
	Takes an array and show the lenth of that array.
	Example:
		input [1,2,3]
		output 3
	"""
	i = 0
	for n in array:
		i = i + 1
	return i

def reverse_array(array):
	"""
	Takes an 1D array and reverses it.
	Example:
		array = [11,12,13]
		reverse_array(array)
		output:
			array = [13,12,11] 
	"""
	new_array = []
	for n in range(own_len(array)):
		new_array.append(array[own_len(array)-n-1])
	return new_array

def reverse_2d_arrays_row(array, row):
	"""
	Takes an 2D array and reverses a selected row.
	Example:
		the 'row' is the index of that array
		array = [
				 [11,12,13],
				 [14,16,17],
				 [18,19,20]
				]
		reverse_2d_arrays_row(array, row=0)
		output:
			array = [
					 [13,12,11],
					 [14,16,17],
					 [18,19,20]
					] 
	"""
	new_array = []
	int(row)
	lenth = own_len(array)
	for n in range(lenth):
		new_array.append(array[row][n])
	for i in range(lenth):
		array[row][i] = reverse_array(new_array)[i]
	return array

def reverse_2d_arrays_col(array, col):
	"""
	Takes an 2D array and reverses a selected column.
	Example:
		the 'col' is the index of that array
		array = [
				 [11,12,13],
				 [14,16,17],
				 [18,19,20]
				]
		reverse_2d_arrays_col(array, col=0)
		output:
			array = [
					 [18,12,13],
					 [14,16,17],
					 [11,19,20]
					] 
	"""
	new_array = []
	int(col)
	lenth = own_len(array)
	for n in range(lenth):
		new_array.append(array[n][col])
	for i in range(lenth):
		array[i][col] = reverse_array(new_array)[i]
	return array

def create_sequence_array(number, end):
	"""
	Takes a number and create a array where elements are integer and start from
	that number ends at spcific number.
	Example:
		create_sequence_array(number=1, end=4)
		output:
			[1,2,3,4]
	"""
	f = []
	for n in range(end):
		f.append(number)
		number = number + 1
	return f

def split_array(array, parts=1):
	"""
	Takes an array and split in specific parts and creates an 2D array.
	Example:
		array [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]
		split_array(array, parts=4)
	output:
		array [1,2,3,4]
			  [5,6,7,8]
			  [9,10,11,12]
			  [13,14,15,16]
	"""
	length = own_len(array)
	return [ array[i*length // parts : (i+1)*length // parts] for i in range(parts) ]

def magic_matrix_4X4(number, end,  parts):
	f = create_sequence_array(end=end,number=number)
	int(number)
	array = split_array(f, parts)
	array = reverse_2d_arrays_col(array, 1)
	array = reverse_2d_arrays_col(array, 2)
	array = reverse_2d_arrays_row(array, 1)
	array = reverse_2d_arrays_row(array, 2)
	return array

input_start_number = int(input("Start from: "))
a = magic_matrix_4X4(input_start_number, 16, 4)
for n in range(own_len(a)):
	print(a[n])
magic_number = simple_array_sum(a[0])
print(magic_number)



