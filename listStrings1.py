#This is from the Lists, Strings problem set.

#Problem 1: Write a function that returns the largest element in a list.
y=[]
while 1:
       Response = raw_input("Insert elements here for the largest value. When done, write 'Done': ")
       if Response == "Done":
               print max(y)
               break
        else:
               y.append(Response)
