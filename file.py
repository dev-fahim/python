#!/bin/python3
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):

	val = 0
	for n in range(0, len(ar)):
		val += ar[n-1]
	return val 

print(simpleArraySum([1,2,3,4,10,11]))

# CompareTripltes

def compareTriplets(a, b):
	len_a = len(a)
	len_b = len(b)
	if len_a != len_b:
		return "Tow tuples should contain equal elements!"
	p_alice = 0
	p_bob = 0
	result = []
	for n in range(0, len_a):
		if a[n] > b[n]:
			p_alice += 1
		elif b[n] > a[n]:
			p_bob += 1
			
		result = [p_alice, p_bob]
	return result

a = (17,28,30)
b = (99, 16, 8)
print(compareTriplets(a, b))

""" Calculate and print the sum of the elements in an array, keeping
	in mind that some of those integers may be quite large.
"""

def aVeryBigSum(ar):
	val = 0
	int(val)
	for n in range(0, len(ar)):
		val += ar[n-1]
	return val 

print(aVeryBigSum([5000000, 5000000]))

"""
	Given a square matrix, calculate the absolute 
	difference between the sums of its diagonals.
"""

def diagonalDifference(arr):
	rows_arr = len(arr)
	diag_a = 0
	diag_b = 0
	for n in range(0, rows_arr):
		re = rows_arr-n-1
		diag_b += arr[n][re]
		diag_a += arr[n][n]
	return abs(diag_a - diag_b)

a = [
		[1,2,3,4],
		[4,5,6,8],
		[7,8,9,9],
		[5,8,6,1]
	]
diagonalDifference(a)

"""
	Given an array of integers, calculate the fractions of its 
	elements that are positive, negative, and are zeros. Print 
	the decimal value of each fraction on a new line.
"""

def plusMinus(arr):
	elements = len(arr)
	neg, pos, zer = [], [], []
	for n in arr:
		if n < 0:
			neg.append(n)
		elif n > 0:
			pos.append(n)
		elif n == 0:
			zer.append(n)
	neg, pos, zer = len(neg), len(pos), len(zer)
	rat_neg, rat_pos, rat_zer= neg/elements, pos/elements, zer/elements
	print("%.6f" % rat_pos)
	print("%.6f" % rat_neg)
	print("%.6f" % rat_zer)

arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)

"""
Consider a staircase of size n = 1 :

   #
  ##
 ###
####
Observe that its base and height are both equal 
to , and the image is drawn using # symbols and spaces. 
The last line is not preceded by any spaces.

Write a program that prints a staircase of size .
"""


































