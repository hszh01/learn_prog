import random
number = random.randint(1,100)
# print(number)
print("Guess a number from 1 to 100.")
while 1:
	t = input()
	t = int(t)
	if t<number:
		print("too small")
	elif t>number:
		print("too big")
	else:
		print("you got it!")
		break
