#Problem 1: Write a function that returns the largest element in a list.
#b = 0
#while 1:
#	Response = raw_input("Input a list of numbers to find the largest element in the list. When done, write 'Done'. ")
#	if str(Response) == "Done":
#		print(b)
#		break
#	else:
#		a = int(Response)
#		if a > b:
#			b = a
from __future__ import division
value = 0
for k in range (1, 137400 + 1):
	inSummation = 0.5/k
	value = value + inSummation
print("value = " + str( value))
