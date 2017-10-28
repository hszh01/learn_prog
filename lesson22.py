## Problem 1: Write a program that prints 'Hello World' to the screen. 
#print ("Hello World")

# Problem 2: Write a program that asks the user for their name and greets them with their name.
#name = raw_input("What is your name? ")
#print ("Hello " + name)

# Problem 3: Modify the previous program such that only the users Alice and Bob are greeted with their names.\
#name = raw_input("What is your name? ")
#if name in ["Alice", "Bob"]:
#	print ("Hello " + name)

# Problem 4: Write a program that asks the user for a number n and prints the sum of numbers 1 to n
#n = int(input("Insert number here. "))
#if n < 0:
#	print("Sorry, I can't find the sum of numbers 1 to " + n)
#elif n == 0:
#	print("Sorry, I can't find teh sum of numbers 1 to " + n)
#elif n > 0:
#	sum = n * (n+1)/2
#	print(sum)

# Problem 5: Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n = 17
#n = int(input("Insert number here. "))
#if n < 0:
#	print("Sorry, I can't find the sum.")
#elif n == 0:
#	print("0")
#elif n > 0:
#	sum = 0
#	for x in range(1, n+1):
#		print(x)
#		if x % 3 == 0:
#			sum = sum + x
#		elif x % 5 == 0:
#			sum = sum + x
#		elif x % 15 == 0:
#			sum = sum - x
#	print(sum)

# Problem 6: Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product 1, ..., n.
#n = int(input("Insert number here. "))
#a = raw_input("Do you want to compute the sum or product? Reply Sum for sum and Product for product. ")
#if a in ["Sum", "sum"]:
#	if n <= 0:
#		print("Sorry, I can't find the sum of numbers 1 to " + n + ".")
#	elif n > 0:
#		sum = n * (n+1)/2
#		print(sum)
#elif a in ["Product", "product"]:
#	if n < 0:
#		print("Sorry, I don't understand your number. Please use a positive number.")
#	if n == 0:
#		print("1")
#	if n > 0:
#		factorial = 1
#		for x in range (1, n+1):
#			print(x)
#			factorial = factorial * x
#		print(factorial)
#else:
#	print("Sorry, I don't understand that.")

# Problem 7: Write a program that prints a multiplication table for numbers up to 12.
#print("This is a multiplication table for numbers up to 12:")
#for y in range (1, 13):
#	z = " "
#	for x in range (1, 13):
#		xy = str(x * y)
#		z = z + " " + xy
#	print z

# Problem 8: Write a program that prints all prime numbers.
#z = int(input("Insert a number for all primes up to that number: "))
#for n in range(1, z+1):
#	isPrime = False
#	for x in range (2, n):
#		p = n % x
#		if p == 0:
#			isPrime = False
#			break
#		else:
#			isPrime = True
#	if isPrime == True:
#		print(n)

# Problem 9: Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed.
#import random
#print("This is a guessing game. Guess the number I am thinking of from 1 to 100.")
#n = random.randint(1, 100)
#v = 0
#while 1:
#	t = int(input("Guess a number from 1 to 100: "))
#	if t < n:
#		print("Too Small!")
#		v = v + 1
#	elif t > n:
#		print("Too Big!")
#		v = v + 1
#	else:
#		print("You got it!")
#		v = v + 1
#		w = str(v)
#		print("It took you " + w + " tries!")
#		break

# Problem 10: Write a program that prints the next 20 leap years.
#print("This program will tell you the next 20 leap years.")
#isLeap = False
#leap = int(input("Insert year here: "))
#for nextLeap in range(leap, 80 +  leap + 1):
#	if nextLeap % 4 == 0:
#		if nextLeap % 400 == 0:
#			isLeap = True
#		elif nextLeap % 100 == 0:
#			isLeap = False
#		else:
#			isLeap = True
#	elif nextLeap % 4 != 0:
#		isLeap = False
#	if isLeap == True:
#		print(nextLeap)

# Problem 11: Write a program that computes ...
from __future__ import division
print("This is a program that computes the problem in Problem 11 of Elementary Problems.")
value = 0
for k in range(1, 10**6 + 1):
	inSummation = 4*((-1)**(k+1)/(2 * k-1))
	value = value + inSummation
#	print((-1)**(k+1) , '--' , (2*k-1) , '--' , inSummation)
print("value = " + str( value))
