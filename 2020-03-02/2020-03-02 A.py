'''
[Hard]
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def LowestMissingPositive(array):
	array.sort()

	positives = [i for i in array if i > 0]

	found = False 
	i = 0

	while not found:
		if i == 0:
			if positives[i] > 1:
				found = True
				return(1)
		elif (positives[i] - positives[i-1]) > 1:
			found = True
			return(positives[i-1] + 1)
		elif i == (len(positives) -1):
			found = True
			return(positives[i] + 1)
		i += 1

myArrays = {"array1" : [3, 4, -1, 1],
	     "array2" : [1, 2, 0],
	     "array3" : [1, 5, -3, -2, 6, 4, 0, 1]}

for key, value in myArrays.items():
	print("Lowest missing positive integer in ", value, " is ", LowestMissingPositive(value), "\n")
