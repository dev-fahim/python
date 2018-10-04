#!/bin/python3
def plen(array):
	i = 0
	for n in array:
		i = i + 1
	return i

def reverse_array(array):
	new_array = []
	for n in range(plen(array)):
		new_array.append(array[plen(array)-n-1])
	return new_array

def reverse_2d_arrays_col(array, col):
	new_array = []
	int(col)
	lenth = plen(array)
	for n in range(lenth):
		new_array.append(array[n][col])
	for i in range(lenth):
		array[i][col] = reverse_array(new_array)[i]
	return array

def create_sequence(n, number):
	f = []
	for n in range(n):
		f.append(number)
		number = number + 1
	return f

def magic_matrix(number):
	f = []
	array_2d = []
	int(number)
	for n in range(4):
		create_sequence(4, number)
		number = number + 1
	for i in range(4):
		array_2d.append(f)
	return array_2d

a = [
		[1,2,3,4],
		[4,5,6,8],
		[7,8,9,9],
		[5,8,6,1]
	]
new_array = reverse_2d_arrays_col(a, 1)
print(new_array)
print(magic_matrix(1))