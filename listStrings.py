#This is all the Lists, Strings Problems.

#Problem 1: Write a function that returns the largest element in a list.
#y=[]
#while 1:
#	Response = raw_input("Insert elements here for the largest value. When done, write 'Done': ")
#	if Response == "Done":
#		print max(y)
#		break
#        else:
#		y.append(Response)
#

#Problem 2: Write a function that reverses a list, preferably in place.
#y=[]
#while 1:
#        Response = raw_input("Insert elements here to reverse the order. Type 'Done' when Done: ")
#        if Response == "Done":
#                y.reverse()
#                print y
#                break
#        else:
#                y.append(Response)

#Problem 3: Write a function that checks whether an element occurs in a list
#y=[]
#while 1:
#        Response = raw_input("Insert elements here for storage. Type 'Done' when Done: ")
#        if Response == "Done":
#                break
#        else:
#                y.append(Response)
#while 2:
#        Response2 = raw_input("Type an element to check if it is in your list: ")
#        if Response2 in y:
#                print "Yes, " + str(Response2) + " is in your list."
#                break
#        else:
#                print "Sorry, " + str(Response2) + " is not in your list."
#                break

#Problem 4: Write a function that returns the element on odd positions in a list
#y=[]
#while 1:
#        Response = raw_input("Insert elements here to find the odd positions in the list. Type 'Done' when Done: ")
#        if Response == "Done":
#                z = y[0::2]
#                print z
#                break
#        else:
#                y.append(Response)

#Problem 5: Write a function that computes the running total of a list
#y=[]
#runningTotal = 0
#while 1:
#        Response = raw_input("Insert elements here to find the running total of the list. Type 'Done' when Done: ")
#        if Response == "Done":
#                for x in range(0, len(y)):
#                        runningTotal = int(runningTotal) + int(y[x])
#                print runningTotal
#                break
#        else:
#                y.append(Response)
