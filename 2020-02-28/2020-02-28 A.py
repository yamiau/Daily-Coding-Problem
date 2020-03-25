'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
from numpy.random import randint

numList = []
n = int(input("Enter the length of our random number list: "))

for i in range(n):
	numList.append(randint(0, 100))
	
print(numList)

k = int(input("Enter the number you want to check: "))

found = False

for i in numList:
	if (k - i) in numList:
		found = True
		break

if (found):
	print("\nThere are two numbers in this list that add up to %d!" % k)
else:
	print("\nThere are no two numbers in this list that add up to %d!" % k)